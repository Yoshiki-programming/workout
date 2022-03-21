from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = "workout_app"

index_view = views.TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('logined/', login_required(index_view), name="index")
]
