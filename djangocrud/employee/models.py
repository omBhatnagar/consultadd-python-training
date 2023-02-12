from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='EMP_ID')
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.emp_id} - Name: {self.name}"