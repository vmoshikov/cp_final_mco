from django.shortcuts import render

from crm.models import Vacancy

def tests(request):
      return render(request, 'demo_task.html', context={'data': "data"})

def test_page(request, vacancy_id, ca_id):

      vacancy = Vacancy.objects.get(id=vacancy_id)
      test = vacancy.testing
      test_type = test.type
      data = {
            "vacancy": vacancy,
            "test": test,
            "test_type": test_type
      }
      return render(request, 'task.html', context={'data': data})