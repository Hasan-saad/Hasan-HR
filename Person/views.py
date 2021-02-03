from django.contrib.auth.decorators import login_required
from . models import Personal, Management, Vacation
from .filters import PersonFilter
from .forms import AddEmploey, AddVacation
from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import DurationField, ExpressionWrapper, F
from django.test import TestCase
import datetime
from datetime import timedelta
from django.utils import timezone
from django.db.models import Avg, Max, Min, Sum

@login_required
def all_emploeys(request):
	all_emploeys = Personal.objects.all()

	myFilter = PersonFilter(request.GET, queryset = all_emploeys)
	all_emploeys = myFilter.qs
	
	paginator = Paginator(all_emploeys, 4)  # Show 25 contacts per page.
	pageNumber = request.GET.get('page') 

	pagePaginator = paginator.get_page(pageNumber)

	context = {'emploeys': pagePaginator, 'filter': myFilter, 'count_Emploey': all_emploeys}
	return	render(request,'Person/all_emploey.html',context)

@login_required
def add_vacatoin(request,id):
				person_detail = Personal.objects.get(id = id)
			
				if request.method == 'POST':
						formVacation = AddVacation(request.POST)
						if formVacation.is_valid():
								myform = formVacation.save(commit=False)
								myform.name = person_detail
								myform.save()
								
								return redirect(reverse('person:all_emploeys'))
								
				else:    
						formVacation = AddVacation()

				
				context = {
					'formVacation':formVacation,
					'person_detail':person_detail,
				}
				return render(request,'Person/vacation.html',context)


@login_required
def person_detail(request, id):
    
	person_detail = Personal.objects.get(id = id)
	count_vcation = Vacation.objects.filter(name_id = person_detail).aggregate(Sum('vacation_num'))
	num_vacation_unavailable = Vacation.objects.filter(name_id = person_detail,vacation__exact='D').aggregate(Sum('vacation_num'))

	count_vacation = count_vcation['vacation_num__sum']
	vacation_unavailable = num_vacation_unavailable['vacation_num__sum']

	if not vacation_unavailable == None:
			person_detail.vacations += vacation_unavailable
	else:
			vacation_unavailable = 0

	if not count_vacation == None:
			betwen = person_detail.vacations - count_vacation
	else:
			betwen = 21
			count_vacation = 0
	num_vacation = person_detail.vacations

	context = { 
		'person_detail': person_detail,
		'num_vacation':num_vacation,
		'count_vacation':count_vacation,
		'betwen':betwen,
		'vacation_unavailable':vacation_unavailable,
		
		
	}
	return render(request,'Person/emploey_details.html',context)

@login_required
def add_person(request):
    if request.method == 'POST':
        personForm = AddEmploey(request.POST, request.FILES)
        if personForm.is_valid():         
            formPerson = personForm.save()
            
            return redirect(reverse('person:all_emploeys'))
    else:
        personForm = AddEmploey()
    context = { 'personForm': personForm}
    return render(request, 'Person/Post_service.html', context)



