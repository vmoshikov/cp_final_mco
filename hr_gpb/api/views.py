from django.shortcuts import render, get_object_or_404

from crm.models import Vacancy, Candidate, Skill
from crm.forms import CandidateApplicationForm

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
                  # print(candidate_request.subject)
                  candidate_request.save()
      else:
            print('Пустая форма')
            vacancy_form = CandidateApplicationForm(vacancy_id)
            
            # print(vacancy_form['form'])
      # vacancy_form = CandidateApplicationForm(request.POST, request.FILES, vacancy_id=vacancy_id)

      return render(request, 'gazprom_vacansy_item.html', context={'data': vacancy, 'form': vacancy_form})