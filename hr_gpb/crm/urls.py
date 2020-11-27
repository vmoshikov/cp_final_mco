from django.urls import include, path
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'ym_tokens', views.YandexOAuthViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'crm'

urlpatterns = [
      path('',  views.index, name='crm_index'),
      path('vacancies/',  views.vacancies_list, name='vacancies_list'),
      path('vacancies/detail/<int:vacancy_id>', views.vacancies_detail, name='vacancy_details'),

      path('candidates/',  views.candidates_list, name='candidates_list'),
      path('candidates/detail/<int:candidat_id>', views.candidates_detail, name='candidat_details'),

]