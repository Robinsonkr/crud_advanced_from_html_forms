from django.db import models
from datetime import datetime, date
 
class Employee(models.Model):
    name  = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    status = models.BooleanField(default=True)
    description = models.TextField(blank=True,null=True)
    created_date=models.DateField(auto_now_add=True)
    website = models.URLField('Website Address',blank=True)
    EMPLOYEE_MODE = (
    ('FULLTIME', 'Fulltime'),
    ('PARTTIME', 'Parttime'),
    ('OUTSOURCING', 'Outsourcing'),  

    )
    mode = models.CharField(choices=EMPLOYEE_MODE,max_length=100)
    department = models.ForeignKey("Department",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee_images/',default='default.jpg',null=True,
                        blank=True,)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=20,null=False,unique=True)

    def __str__(self):
        return self.name



