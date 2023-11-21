
from django.shortcuts import render,redirect
from Faker_App.models import Employee

from faker import Faker
fakerObject = Faker()

def create_employee_fake_data_view(request):
    for i in range(20):
        first_name = fakerObject.first_name()
        last_name = fakerObject.last_name()
        city = fakerObject.random_element(elements=('Delhi','Hyderabad','Pune','Mumbai'))
        role = fakerObject.random_element(elements=('PM','TL','SE','HR'))
        salary = fakerObject.random_element(elements=(10000,20000,30000,40000))
        email = fakerObject.email()

        Employee.objects.create(
            first_name=first_name, last_name=last_name,city=city,
            role=role, salary=salary,email=email
        )
    return redirect('accessing_fakedata') # alice name calling
    # return redirect('/accessing/fake/data/') # Direct url name calling
    # return redirect(accessing_employee_fake_data_view) # View Name calling


from django.core.paginator import Paginator
from django.core import paginator

def accessing_employee_fake_data_view(request):
    employee_list = Employee.objects.all()
    p = Paginator(employee_list, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except paginator.PageNotAnInteger:
        page_obj = p.page(1)
    except paginator.EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        "employee_list" : employee_list,
        "page_obj": page_obj
    }
    return render(request,'accessing_employee.html', context)


