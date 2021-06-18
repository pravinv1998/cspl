from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import *
from .filter import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from .decorators import *
from django.contrib.auth.decorators import login_required

import csv

from django.http import HttpResponse, response

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'customer/home.html')

@login_required(login_url='login')
def index(request):  
    form = VisitsForm(request.POST or None) 
    if form.is_valid():
        form.save()
        form = VisitsForm()
    return render(request, 'customer/index.html',{
        'form':form
    }) 
    # return render(request, 'customer/login.html') 

@login_required(login_url='login')
def addCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()
    return render(request, 'customer/addCustomer.html', {
        'form':form
    })    





@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def allCustomers(request):
    customers = Customer.objects.all().order_by('-id')
    customer_count = customers.count()
    if request.method == 'GET':
        custfilter = CustomerFilter(request.GET, queryset=customers)
        customers = custfilter.qs
        custfilter = CustomerFilter()
    return render(request, 'customer/allCustomer.html',{
        'customers': customers,
         'custfilter': custfilter,
         'customer_count': customer_count,
    })

@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def allVisits(request):
    visit = Visits.objects.all().order_by('-id')
    visits_count = visit.count()
        
    if request.method == 'GET':
        visitfilter = VisitsFilter(request.GET, queryset=visit)
        visit = visitfilter.qs
        visitfilter = VisitsFilter()
    return render(request, 'customer/allVisits.html',{
        'visit': visit,
         'visitfilter': visitfilter,
         'visits_count': visits_count,
    })

@login_required(login_url='login')
def customerVisits(request,pk):
    visit = Visits.objects.all().filter(id=pk)
    return render(request, 'customer/customerVisits.html',{
        'visit': visit,
    })


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request, 'customer/login.html')

@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('/')
    


##################################################################
@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customer.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Address', 'City', 'State','Phone No','Email','Created Date'])

    customers = customers.values_list('name', 'addr', 'city', 'state','phone','email','created_date')
    for customer in customers:
        writer.writerow(customer)

    return response
##############################################################


# def customerFilter(request):
#     if request.method == 'GET':
#         customer = Customer.objects.all()
#         custfilter = CustomerFilter(request.GET, queryset=customer)
#         customer = custfilter.qs

    
#     return render(request, 'customer/allCustomer.html', {
#         'custfilter': custfilter,
#         'customer': customer
#     })

# def visitsFilter(request):
#     if request.method == 'GET':
#         visit = Visits.objects.all()
#         visitfilter = CustomerFilter(request.GET, queryset=visit)
#         visit = visitfilter.qs

    
#     return render(request, 'customer/allCustomer.html', {
#         'visitfilter': visitfilter,
#         'visit': visit,
#     })

@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    visits = customer.visits_set.all().order_by('-id')
    visits_count = visits.count()

    myfilter = VisitsFilter(request.GET, queryset=visits)
    visits = myfilter.qs
    myfilter = VisitsFilter()

    return render(request, 'customer/customer.html', {
        'visits': visits,
        'visits_count': visits_count,
        'myfilter': myfilter,
        'customer': customer,
    })


@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)  

    if request.method == 'POST':
        customer.delete()
        return redirect('allCustomers')

    return render(request, 'customer/delete_customer.html',{
        'item': customer,
    })
