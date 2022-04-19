from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "api"

urlpatterns = [
    path('workouts/', views.WorkoutListAPI.as_view()),
    path('workouts/<int:pk>/', views.WorkoutDetailAPI.as_view()),
    path('workout-records/', views.WorkoutRecordlistAPI.as_view()),
    path('workout-record-detail/<int:pk>', views.WorkoutRecordDetailAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)