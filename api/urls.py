from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "api"

urlpatterns = [
    path('workouts/', views.WorkoutListAPI.as_view()),
    path('workouts/<int:pk>/', views.WorkoutDetailAPI.as_view()),
    path('workout-records/<int:workout>/', views.WorkoutRecordlistAPI.as_view()),
    path('workout-records/<int:pk>/record/', views.WorkoutRecordDetailAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)