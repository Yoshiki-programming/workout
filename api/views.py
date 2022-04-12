from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, filters, authentication, status
from workout_app.models import Workout, WorkoutDetail
from .serializers import MypageSerializer, WorkoutDetailSerializer, WorkoutSerializer, UserSerializer
from django.shortcuts import redirect
User = get_user_model()
# Create your views here.

class MyPageViewSet(viewsets.ReadOnlyModelViewSet):
    # 今までのトレーニング成果を表示
    # 編集不可
    # ユーザー情報の表示
    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = MypageSerializer
    # queryset = WorkoutDetail.objects.all()
    def get_queryset(self):
        self.user = self.request.user
        return WorkoutDetail.objects.filter(workout__user=self.user)
    
class WorkoutCreateViewSet(viewsets.ModelViewSet):
    # ワークアウトを追加
    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = WorkoutSerializer
    def get_queryset(self):
        self.user = self.request.user
        return Workout.objects.filter(user=self.user)
    
class RecordViewSet(viewsets.ModelViewSet):
    # ワークアウトの記録をしていく
    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = WorkoutDetailSerializer
    def get_queryset(self):
        self.user = self.request.user
        return Workout.objects.filter(user=self.user)
