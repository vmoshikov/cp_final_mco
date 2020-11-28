from django.shortcuts import render, get_object_or_404
import sys, os, json

from .models import Vacancy, Skill, Candidate, CandidateApplication
from api.views import send_notification

# ДЕМО
from pdfminer.high_level import extract_text

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



def index(request):
      return render(request, 'index.html', context={"data": 'data'})

def vacancies_list(request):

    all_vacancys = Vacancy.objects.all()

    # При отсутствующей авторизации
    # try:
    #     my_vacancys = Vacancy.objects.filter(owner = request.user)
    # except:
    #     my_vacancys = Vacancy.objects.all()

    data = {
        'all_vacancys': all_vacancys,
        # 'my_vacancys': my_vacancys
    }

    return render(request, 'vacancy.html', context={'data': data})

def vacancies_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)

    data = {
        "vacancy": vacancy,
        "vacancy_requests": {
            "new": CandidateApplication.objects.filter(core_vacancy=vacancy, status=1),
            "tests": CandidateApplication.objects.filter(core_vacancy=vacancy, status=2),
            "interview": CandidateApplication.objects.filter(core_vacancy=vacancy, status=3),
            "secure": CandidateApplication.objects.filter(core_vacancy=vacancy, status=4),
            "offer": CandidateApplication.objects.filter(core_vacancy=vacancy, status=5),
            "decline": CandidateApplication.objects.filter(core_vacancy=vacancy, status=0)
        },
    }
    
    return render(request, 'vacancy_detail.html', context={'data': data})


def candidates_list(request):
    all_candidates = Candidate.objects.all()

    data = {
        'all_candidates': all_candidates,
        # 'my_candidates': my_candidates
    }

    return render(request, 'candidates.html', context={'data': data})

def candidates_detail(request, candidat_id):
    return render(request, 'candidates.html', context={'data': 'data'})



# Дебаг
def ca_details(request, ca_id):

    ca = get_object_or_404(CandidateApplication, id=ca_id)

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
    

    return render(request, 'demo_data.html', context={'data': json.dumps(candidate_conformity)})



def demo_task(request):
    return render(request, 'demo_task.html', context={'data': "data"})