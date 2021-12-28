from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

class CalculatorView(APIView):
    
    def get(self,request):
            return Response({'data':'data'}, content_type="application/json")
