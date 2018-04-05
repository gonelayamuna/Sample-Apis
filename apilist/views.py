from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView



class SignupView(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignupSerializer



class EnquiryViewOld(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

class EnquiryView(APIView):


    def get(self, request, format=None):
        snippets = Enquiry.objects.all()
        serializer = EnquirySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MhlEnquiryView(APIView):


    def get(self, request, format=None):
        snippets = MhlEnquiry.objects.all()
        serializer = MhlEnquirySerailizer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MhlEnquirySerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

