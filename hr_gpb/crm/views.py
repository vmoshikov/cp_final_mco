from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
import sys, os, json

from .models import Vacancy, Skill, Candidate, CandidateApplication
from .forms import AddVacancyForm

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

    data = {
        "StagesApplications": [CandidateApplication.objects.filter(status=1).count(), CandidateApplication.objects.filter(status=2).count(), CandidateApplication.objects.filter(status=3).count(), CandidateApplication.objects.filter(status=4).count(),]
    }
    
    return render(request, 'index.html', context={"data": data})

def vacancies_list(request):

    all_vacancys = Vacancy.objects.all()

    application_stat = []
    print(all_vacancys)
    for vacancy in all_vacancys:
        ca = CandidateApplication.objects.filter(core_vacancy=vacancy).values('status').annotate(dcount=Count('status'))

        application_stat.append(list(ca.values_list('dcount', flat=True)))

    print(application_stat)

    # При отсутствующей авторизации
    # try:
    #     my_vacancys = Vacancy.objects.filter(owner = request.user)
    # except:
    #     my_vacancys = Vacancy.objects.all()

    vacancy_data = zip(all_vacancys, application_stat)
    data = {
        "all_vacancys": all_vacancys,
        "application_stat": application_stat,
        "vacancy_data": vacancy_data
        # 'my_vacancys': my_vacancys
    }

    return render(request, 'vacancy.html', context={'data': data})

def add_vacancy(request):

    if request.method == "POST":

            vacancy_form = AddVacancyForm(request.POST)

            if vacancy_form.is_valid():
                print('Форма ВАЛИДНА')
                add_vacancy = vacancy_form.save(commit=False)

                send_notification(f'{add_vacancy.owner}, вакансия по вашему запросу создана \nРекрутер вакансии: {add_vacancy.recruter}\nКод-ревью проводит {add_vacancy.code_reviewer}')
                add_vacancy.save()

    data = {
        "form": AddVacancyForm()
    }
   
    return render(request, 'add_vacancy.html', context={'data': data})

@csrf_exempt
def vacancies_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == "POST":
        ca = CandidateApplication.objects.get(id=request.POST['application'])
        if request.POST['status'] == 'trash':
            ca.status = 0
        else:
            ca.status += 1
        
        ca.save()

    data = {
        "vacancy": vacancy,
        "vacancy_requests": {
            "new": CandidateApplication.objects.filter(core_vacancy=vacancy, status=1),
            "interview": CandidateApplication.objects.filter(core_vacancy=vacancy, status=2),
            "secure": CandidateApplication.objects.filter(core_vacancy=vacancy, status=3),
            "offer": CandidateApplication.objects.filter(core_vacancy=vacancy, status=4),
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