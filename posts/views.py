from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "index.html"