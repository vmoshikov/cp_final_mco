from django import forms

from .models import TestingSolution

class TestingSolutionForm(forms.ModelForm):

      class Meta:
                  model = TestingSolution
                  fields = ('description', 'link', 'file' )

                  labels = {
                        'description': "Краткое описание решения",
                        'link': "Ссылка на решение",
                        'file': "Файл",
                  }

class TestingReviewForm(forms.ModelForm):

      class Meta:
                  model = TestingSolution
                  fields = ('reviewer_comment', 'status', )

                  labels = {
                        'reviewer_comment': "Комментарий ревьювера",
                        'status': "Статутс",
                  }
