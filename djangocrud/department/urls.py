from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDepartments),
    path('createdept', views.createDepartment),
    path('<id>/update', views.updateDepartment),
    path('<id>/delete', views.deleteDepartment),
]