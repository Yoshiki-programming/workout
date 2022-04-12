from . import views
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth.decorators import login_required
app_name = "api"

router = routers.DefaultRouter()
router.register(r'workout', views.WorkoutCreateViewSet, basename="workout")
router.register(r'mypage', views.MyPageViewSet, basename="mypage")
router.register(r'record', views.MyPageViewSet, basename="record")

urlpatterns = [
    path('', include(router.urls)),
]