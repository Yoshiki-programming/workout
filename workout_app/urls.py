from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = "workout_app"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('mypage/', login_required(views.MyPageView.as_view()), name="mypage"),
    path("record/", login_required(views.WorkoutCreateView.as_view()), name="record"),
]
