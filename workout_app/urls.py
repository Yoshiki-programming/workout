from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "workout_app"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("", views.MypageView.as_view(), name="top"),
]
