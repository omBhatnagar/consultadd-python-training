from django.urls import path
from . import views

urlpatterns=[
    path('', views.viewEmployees),
    path('createemployee', views.createEmployee),
    path('<id>/update', views.updateEmployee),
    path('<id>/delete', views.deleteEmployee),
]