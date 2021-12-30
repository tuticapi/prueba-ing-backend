from django.urls import path
from rest_framework import routers
from .views import CalculatorView

app_name = 'calculator'
router = routers.DefaultRouter()
urlpatterns = [
    path('', CalculatorView.as_view(),name='calculate_team_salary'),
]
urlpatterns += router.urls