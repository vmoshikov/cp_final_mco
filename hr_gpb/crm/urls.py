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
      path('vacancy/',  views.vacancy, name='crm_vacancy'),
      path('vacancy/details/<int:vacancy_id>', views.vacancy_details, name='vacancy_details'),
]