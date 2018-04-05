from django.contrib import admin

# Register your models here.
from django.contrib import admin
from apilist.models import *
admin.site.register(SignUp)
admin.site.register(Enquiry)
admin.site.register(MhlEnquiry)