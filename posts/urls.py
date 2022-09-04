from xml.etree.ElementInclude import include
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home")
]
