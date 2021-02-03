from django.urls import path, include
from .views import *

app_name = 'Person'


urlpatterns = [
    path('', all_emploeys, name = 'all_emploeys'),
    path('<int:id>/', person_detail, name = 'emploey_details'),
    path('add/', add_person, name='add_person'),
    path('<int:id>/vacation/', add_vacatoin, name='add_vacation'),
    
]