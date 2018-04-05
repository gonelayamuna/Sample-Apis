from django.conf.urls import url,include
from apilist import views
from rest_framework import routers
from django.contrib import admin
from .views import *

router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'api/signup', views.SignupView)
router.register(r'api/enquiryold', views.EnquiryViewOld)

admin.autodiscover()

urlpatterns = [
    url(r'^',include(router.urls)),
   # url(r'^api/enq', EnquiryView.as_view({'get':'create'})),
    url(r'api/enquiry',EnquiryView.as_view()),
    url(r'api/submitted',MhlEnquiryView.as_view()),
]