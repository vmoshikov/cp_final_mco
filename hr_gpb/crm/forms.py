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
