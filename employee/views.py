from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


@login_required(login_url='login')
def display_employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employees": employees})


@login_required(login_url='login')
def employee_create(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return redirect("employees")
    else:
        employee_form = EmployeeForm()
    return render(request, "employee/create.html", {"employee_form": employee_form})


@login_required(login_url='login')
def employee_edit(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == "POST":
        # After editing: get data from formAyaz
        # Note the second argument: the meeting we are editing
        employee_form = EmployeeForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            # redirect back to detail page after save
            return redirect("employees")
        else:
            # Pre-fill the form with data from existing meeting
            employee_form = EmployeeForm(instance=employee)
            return render(request, "employee/edit.html", {"employee_form": employee_form})
    else:
        # Pre-fill the form with data from existing meeting
        employee_form = EmployeeForm(instance=employee)
        return render(request, "employee/edit.html", {"employee_form": employee_form})


@login_required(login_url='login')
def employee_delete(request, id):
    emp_id = int(id)
    try:
        emp_selected = get_object_or_404(Employee, pk=emp_id)
    except Employee.DoesNotExist:
        return redirect('employees')
    emp_selected.delete()
    return redirect('employees')


@login_required(login_url='login')
def employee_details(request, id):
    employee = get_object_or_404(Employee, pk=id)
    return render(request, "employee/details.html", {"employee": employee})
