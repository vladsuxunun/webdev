from django.urls import path

from . import views
from .views import companies_list,company_details,company_vacancies,vacancies_list,vacancy_details,vacancies_top_ten

urlpatterns = [
    path('companies/',companies_list),
    path('companies/<int:company_id>/',company_details),
    path('companies/<int:company_id>/vacancies',company_vacancies),
    path('vacancies/',vacancies_list),
    path('vacancies/<int:vacancy_id>/',vacancy_details),
    path('vacancies/top_ten/',vacancies_top_ten),
]