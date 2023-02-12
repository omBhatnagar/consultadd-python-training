from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def viewEmployees(request):
    context = {}
    context['dataset'] = Employee.objects.all()
    return render(request, "employee_list.html", context)

def createEmployee(request):
    context ={}
 
    # add the dictionary during initialization
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_employee.html", context)

def updateEmployee(request, id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Employee, emp_id = id)
 
    # pass the object as instance in form
    form = EmployeeForm(request.POST or None, instance = obj)

    #save and redirect
    if form.is_valid():
        form.save()
        return HttpResponse("Updated succesfully!")
 
    context["form"] = form
 
    return render(request, "update_employee.html", context)

def deleteEmployee(request, id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Employee, emp_id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # send response after deleting
        return HttpResponse("Deleted successfully!")
 
    return render(request, "delete_employee.html", context)