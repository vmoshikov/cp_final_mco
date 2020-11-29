from django.urls import include, path
from . import views

# router = routers.DefaultRouter()
# router.register(r'ym_tokens', views.YandexOAuthViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'tests'

urlpatterns = [
      path('',  views.tests, name='tests'),
      path(f'task/<int:vacancy_id>:<int:ca_id>',  views.test_page, name='test_page'),
      path(f'review/<int:vacancy_id>:<int:ca_id>',  views.review_page, name='review_page'),

]