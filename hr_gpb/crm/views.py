from django.shortcuts import render


def index(request):
      return render(request, 'index.html', context={"data": 'data'})

def vacancy(request):
      return render(request, 'vacancy.html', context={"data": 'data'})

def vacancy_details(request):
      return render(request, 'vacancy_deatail.html', context={"data": 'data'})
