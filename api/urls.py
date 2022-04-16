from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "api"

urlpatterns = [
    path('workout/', views.WorkoutList.as_view()),
    path('workout/record/<int:pk>/', views.Recordlist.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)