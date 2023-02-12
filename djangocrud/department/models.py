from django.db import models
from employee.models import Employee

# Create your models here.
class Department(models.Model):
    department_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='DEPT ID')
    department_name = models.CharField(max_length=64)
    emp_id = models.ForeignKey(Employee, null=False, on_delete=models.CASCADE, verbose_name='Manager ID')
    
    def __str__(self):
        return f"{self.department_id}: Nam: {self.department_name}, Manager ID: {self.emp_id}"

    