from django.urls import include, path
from . import views

urlpatterns = [
    path('vacancy_list/', views.vacancy_list, name='vacancy_list'),
    path('vacancy_list/<str:vacancy_id>', views.vacancy_page, name='vacancy_page')
    
]