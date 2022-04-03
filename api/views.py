from pyexpat import model
from re import template
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from rest_framework import generics, viewsets, filters, authentication, response
from workout_app.models import Workout, WorkoutDetail
from .serializers import WorkoutDetailSerializer, WorkoutSerializer
from django.shortcuts import redirect
User = get_user_model()
# Create your views here.

class MyPageViewSet(viewsets.ViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = WorkoutDetailSerializer
    # queryset = WorkoutDetail.objects.all()
    def list(self, request):
        queryset = WorkoutDetail.objects.filter(workout__user=request.user)
        serializer = WorkoutDetailSerializer(queryset, many=True)
        return response.Response(serializer.data)

class WorkoutCreateViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = WorkoutSerializer
    def get_queryset(self):
        self.user = self.request.user
        return Workout.objects.filter(user=self.user)
    
class RecordViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = WorkoutDetailSerializer
    def get_queryset(self):
        self.user = self.request.user
        return Workout.objects.filter(user=self.user)