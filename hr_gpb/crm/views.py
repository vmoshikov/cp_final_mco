from django.shortcuts import render, get_object_or_404
import sys

from .models import Vacancy, Skill, Candidate

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
            "new": "new",
            "tests": "tests",
            "interview": "interview",
            "secure": "secure",
            "offer": "offer",
            "decline": "decline"
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