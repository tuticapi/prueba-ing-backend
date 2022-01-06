from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .core import Core
from .serializers import MemberSerializer, MemberSalarySerializer

# Create your views here.


class CalculatorView(APIView):

    def post(self, request):
        data = request.data
        if('jugadores' not in data):
            return Response({"error": "missing information"},
                            content_type="application/json",
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = MemberSerializer(data=data.get('jugadores'), many=True)
        serializer.is_valid(raise_exception=True)
        core = Core(serializer.data)
        team_salaries = core.calculate_salary()
        team = MemberSalarySerializer(data=team_salaries, many=True)
        team.is_valid(raise_exception=True)
        return Response(team.data,
                        content_type="application/json",
                        status=status.HTTP_200_OK)
