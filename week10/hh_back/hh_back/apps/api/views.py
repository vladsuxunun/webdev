from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from . models import Company,Vacancy

# Create your views here.

def companies_list(request):
    companies_list = Company.objects.order_by('id')
    companies_list_json = [company.short() for company in companies_list]
    return JsonResponse(companies_list_json, safe=False)

def company_details(request, company_id):
    try:
        company=Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse(company.full(),safe=False)

def company_vacancies(request, company_id):
    try:
        company_vacancies = Vacancy.objects.filter(company_id = company_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    vacansies_json=[vacancy.short() for vacancy in company_vacancies]

    return JsonResponse(vacansies_json,safe=False)

def vacancies_list(request):
    vacancies_list = Vacancy.objects.order_by('id')
    vacancies_list_json = [vacancy.short() for vacancy in vacancies_list]
    return JsonResponse(vacancies_list_json,safe=False)

def vacancy_details(request, vacancy_id):
    try:
        vacancy=Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse(vacancy.full(),safe=False)

def vacancies_top_ten(request):
    vacancies_top_ten_list= Vacancy.objects.order_by('-salary')[:10]
    vacancies_top_ten_list_json=[vacancy.full() for vacancy in vacancies_top_ten_list]
    return JsonResponse(vacancies_top_ten_list_json,safe=False)