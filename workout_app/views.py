from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, CreateView, ListView
from .forms import SignUpForm
from django.urls import reverse_lazy
from .models import (
    Workout,
    Weight,
    Sets,
    Reps
)
User = get_user_model()
# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
