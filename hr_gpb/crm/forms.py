from django import forms

from .models import Candidate, Vacancy, CandidateApplication


# Прием резюме с сайта
class CandidateApplicationForm(forms.ModelForm):

      candidate_name = forms.CharField(label='Ваше имя')
      phone = forms.CharField(label='Телефон')
      email = forms.EmailField(label='Электронная почта')
      candidate_id = forms.CharField(widget=forms.HiddenInput(), required=False)

      class Meta:
            model = CandidateApplication
            fields = ('cv_file', )

            labels = {
                  'cv_file': "Резюме",
            }


      def __init__(self, vacancy_id, *args, **kwargs):
            super(CandidateApplicationForm, self).__init__(*args, **kwargs)

      def save(self, commit=True):
            
        candidate, created = Candidate.objects.get_or_create(
          email = self.cleaned_data['email'],
          )
        
        if created:
              candidate.fullname = self.cleaned_data['candidate_name']
              print(candidate.fullname)
              candidate.email = self.cleaned_data['email']
              candidate.phone = self.cleaned_data['phone']
              candidate.save()

        return super(CandidateApplicationForm, self).save(commit)


class AddVacancyForm(forms.ModelForm):
      class Meta:
            model = Vacancy
            fields = ('title', 'owner', 'recruter', 'status', 'description', 'duties', 'experience', 'key_skills', 'additional_skills', 'conditions', 'city', 'testing', 'code_reviewer' )

            labels = {
                  'title': 'Заголовок',
                  'owner': 'Заказчик',
                  'recruter': 'Рекрутер',
                  'status': 'Статус',
                  'description': 'Описание',
                  'duties': 'Обязанности',
                  'experience': 'Опыт',
                  'key_skills': 'Ключевые навыки',
                  'additional_skills': 'Вспомогательные навыки',
                  'conditions': 'Условия работы',
                  'city': 'Город',
                  'testing': 'Тестовое задание',
                  'code_reviewer': 'Ответственный за код-ревью'
            }