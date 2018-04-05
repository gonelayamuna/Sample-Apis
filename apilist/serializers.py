from rest_framework import serializers
from apilist.models import *
from django.contrib.auth import authenticate

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignUp
        fields=('id','email','name','password','confirm_password',)

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model=Enquiry
        fields=('name','email','mobile','course_choice',)

class MhlEnquirySerailizer(serializers.ModelSerializer):
    class Meta:
        model=MhlEnquiry
        fields=('name','email','phone','query')

