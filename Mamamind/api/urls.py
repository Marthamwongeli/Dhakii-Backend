from django.urls import path
from .views import api_home  # Import your API view here

urlpatterns = [
    path('', api_home),  # Add your API view route
]
