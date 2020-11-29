from django.shortcuts import render

from crm.models import Vacancy, CandidateApplication

from .models import TestingSolution
from .forms import TestingSolutionForm, TestingReviewForm

def tests(request):
      return render(request, 'demo_task.html', context={'data': "data"})

def test_page(request, vacancy_id, ca_id):

      vacancy = Vacancy.objects.get(id=vacancy_id)
      ca = CandidateApplication.objects.get(id=ca_id)

      test = vacancy.testing
      test_type = test.type

      if request.method == "POST":
            print('Форма отправлена')
            testing_form = TestingSolutionForm(request.POST, request.FILES)
            if testing_form.is_valid():
                  print('Форма ВАЛИДНА')
                  testing_form.save()
                  
                  testing_solution = TestingSolution.objects.last()
                  ca.testing_solution = testing_solution
                  ca.save()


      else:
            print('Пустая форма')
            testing_form = TestingSolutionForm()
      
      data = {
            "vacancy": vacancy,
            "test": test,
            "test_type": test_type,
            "ca": ca,
            "ca_testing_solution": ca.testing_solution,
            "form": testing_form
      }

      return render(request, 'task.html', context={'data': data})

def review_page(request, vacancy_id, ca_id):
      vacancy = Vacancy.objects.get(id=vacancy_id)
      ca = CandidateApplication.objects.get(id=ca_id)

      test = vacancy.testing
      test_type = test.type

      if request.method == "POST":
            review_form = TestingReviewForm(request.POST)
            if review_form.is_valid():
                  print('Форма ВАЛИДНА')
                  review_form.save()

      else:
            print('Пустая форма')
            review_form = TestingReviewForm()
      
      data = {
            "vacancy": vacancy,
            "test": test,
            "test_type": test_type,
            "ca": ca,
            "ca_testing_solution": ca.testing_solution,
            "form": review_form
      }

      return render(request, 'review.html', context={'data': data})