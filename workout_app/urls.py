from django.urls import path,re_path
from . import views

app_name = "workout_app"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("user-update/<int:pk>", views.UserUpdate.as_view(), name="update"),
    path("user-info/<int:pk>", views.UserDetail.as_view(), name="info"),
    path("", views.MypageView.as_view()),
]
