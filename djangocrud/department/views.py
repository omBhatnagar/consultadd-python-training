from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Department
from .forms import DepartmentForm

# Create your views here.
def getDepartments(request):
    context = {}
    context['dataset'] = Department.objects.all()
    return render(request, "dept_list.html", context)

def createDepartment(request):
    context = {}
    
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context['form'] = form
    return render(request, "create_dept.html", context)

def updateDepartment(request, id):
    context = {}
    
    # fetch department
    department = get_object_or_404(Department, department_id = id)
    
    # pass to form
    form = DepartmentForm(request.POST or None, instance = department)
    
    # save
    if form.is_valid():
        form.save()
        return HttpResponse("Updated successfully!")

    context['form'] = form
    
    return render(request, 'update_dept.html', context)

def deleteDepartment(request, id):
    context = {}
    
    # fetch department
    department = get_object_or_404(Department, department_id = id)
    
    if request.method == 'POST':
        # delete
        department.delete()
        # send response after deleting
        return HttpResponse("Deleted successfully!")

    return render(request, "delete_dept.html", context)