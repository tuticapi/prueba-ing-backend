from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .core import Core
from .serializers import MemberSerializer

# Create your views here.

class CalculatorView(APIView):
    
    def post(self,request):
            data = request.data
            if('jugadores' not in data):
                return Response({"error": "missing information"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = MemberSerializer(data=data.get('jugadores'), many=True)
            serializer.is_valid(raise_exception=True)
            core = Core(serializer.data)
            core.calculate_salary()
            return Response({'data':serializer.data}, content_type="application/json")
