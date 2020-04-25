from django.db import models

Gender_Choices = (('M', 'Male'), ('F', 'Female'))
Standard_Choices = ((8, '8th'), (9, '9th'), (10, '10th'))


# Create your models here.
class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=Gender_Choices)
    standard = models.IntegerField(choices=Standard_Choices)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'User : {self.id} | Name : {self.name} | Standard : {self.standard}'
