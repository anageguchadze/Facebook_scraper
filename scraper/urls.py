# scraper/urls.py
from django.urls import path
from .views import get_facebook_data

urlpatterns = [
    path('facebook_data/', get_facebook_data, name='facebook_data'),
]
