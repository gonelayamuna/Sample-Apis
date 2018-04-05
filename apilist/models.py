from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class SignUp(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    email=models.EmailField()
    confirm_password=models.CharField(max_length=15,default=password)

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.IntegerField()
    COURSE_CHOICE=(('aws','Aws'),
                    ('devops','Devops'),
                    ('sa','Solution Architect'))
    course_choice=models.CharField(max_length=10,choices=COURSE_CHOICE)

class MhlEnquiry(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    query=models.CharField(max_length=300)

    def __str__(self):
        return self.name

