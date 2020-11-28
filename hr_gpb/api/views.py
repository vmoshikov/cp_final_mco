import sys, io, json, requests
from django.shortcuts import render, get_object_or_404

from crm.models import Vacancy, Candidate, Skill, CandidateApplication
from crm.forms import CandidateApplicationForm

from pdfminer.high_level import extract_text, extract_text_to_fp

from natasha import (
    Segmenter,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,

    MorphVocab,
    
    Doc, 

    NamesExtractor,
    PER
)

def vacancy_list(request):

      vacancies = Vacancy.objects.all()
      return render(request, 'gazprom_base.html', context={'data': vacancies})

def vacancy_page(request, vacancy_id):

      vacancy = get_object_or_404(Vacancy, id=vacancy_id)

      if request.method == "POST":
            print('Форма отправлена')
            vacancy_form = CandidateApplicationForm(vacancy_id, request.POST, request.FILES)
            print(request.FILES)
            print(vacancy_form)
            if vacancy_form.is_valid():
                  print('Форма ВАЛИДНА')
                  candidate_request = vacancy_form.save(commit=False)
                  candidate_request.core_vacancy = Vacancy.objects.get(id=vacancy_id)
                  candidate_request.core_condidate = Candidate.objects.last()
                  candidate_request.save()

                  candidate_request = CandidateApplication.objects.last()
                  cv_recognition(candidate_request.id)

      else:
            print('Пустая форма')
            vacancy_form = CandidateApplicationForm(vacancy_id)
            
            # print(vacancy_form['form'])
      # vacancy_form = CandidateApplicationForm(request.POST, request.FILES, vacancy_id=vacancy_id)

      return render(request, 'gazprom_vacansy_item.html', context={'data': vacancy, 'form': vacancy_form})

def cv_recognition(candidate_request_id):
      ca = get_object_or_404(CandidateApplication, id=candidate_request_id)
      text = extract_text(ca.cv_file.path)

      ca.cv_recognition = text

      try:
            ca.skills_assessment = calculate_skills_assessment(text, ca)
      except:
            ca.skills_assessment = []
            
      ca.save()

      return True
def calculate_skills_assessment(text, ca):
      vacancy_key_skills = list(map(lambda x:x.lower(),list(ca.core_vacancy.key_skills.all().values_list('title', flat=True))))
      vacancy_additional_skills = list(map(lambda x:x.lower(),list(ca.core_vacancy.additional_skills.all().values_list('title', flat=True))))

      segmenter = Segmenter()
      emb = NewsEmbedding()
      morph_tagger = NewsMorphTagger(emb)
      syntax_parser = NewsSyntaxParser(emb)
      morph_vocab = MorphVocab()

      text = extract_text(ca.cv_file.path)

      doc = Doc(text)

      doc.segment(segmenter)
      doc.tag_morph(morph_tagger)
      doc.parse_syntax(syntax_parser)

      cv_key_skills = []
      cv_additional_skills = []

      for token in doc.tokens:
            token.lemmatize(morph_vocab)
            print(token)
            if token.lemma in vacancy_key_skills and token.lemma not in cv_key_skills:
                  cv_key_skills.append(token.lemma)
                  print(token.lemma)

            if token.lemma in vacancy_additional_skills and token.lemma not in cv_additional_skills:
                  cv_additional_skills.append(token.lemma)
                  print(token.lemma)
      

      candidate_conformity = {
            "key_skills": {
                  "vacancy_key_skills": vacancy_key_skills,
                  "cv_key_skills": cv_key_skills,
                  "conformity_percent": len(cv_key_skills) / len(vacancy_key_skills)
            },
            "additional_skills": {
                  "vacancy_additional_skills": vacancy_additional_skills,
                  "cv_additional_skills": cv_additional_skills,
                  "conformity_percent": len(cv_additional_skills) / len(vacancy_additional_skills)
            }
      }

      return json.dumps(candidate_conformity)

def send_notification(message, format='telegram', to=False):
      requests.get(f'https://api.telegram.org/bot1193004661:AAFAm-XtTHW5BL1YxrIB8IXX9uok6D5RvBA/sendMessage?chat_id=-1001170365685&text={message}')