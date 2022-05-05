from django.contrib.auth import get_user_model
from rest_framework import generics, pagination
from workout_app.models import Workout, WorkoutDetail
from .serializers import UserSerializer, WorkoutDetailSerializer, WorkoutSerializer, MypageSerializer
User = get_user_model()
import logging
 
# Create your views here.

class APIPagination(pagination.PageNumberPagination):
    page_size = 5

# ログインユーザーで筋トレメニューをpost、追加したメニューをgetできる
class WorkoutListAPI(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    pagination_class = APIPagination
    def get_queryset(self):
        user = self.request.user
        return Workout.objects.filter(user=user).order_by("-id")
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 各ユーザー追加して筋トレのメニューの更新、削除
class WorkoutDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    pagination_class = APIPagination
    def get_queryset(self):
        user = self.request.user
        return Workout.objects.filter(user=user).order_by("-id")
    
# リクエストユーザーが保存した筋トレの記録を追加できる、兼マイページ
class WorkoutRecordlistAPI(generics.ListCreateAPIView):
    serializer_class = WorkoutDetailSerializer
    pagination_class = APIPagination
    def get_queryset(self):
        user = self.request.user
        workout = self.kwargs['workout']
        return WorkoutDetail.objects.filter(workout__user=user, workout__id=workout).order_by("-id")
    # def perform_create(self, serializer):
    #     serializer.save()

# ワークアウト記録を更新、削除するapi
class WorkoutRecordDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutDetailSerializer
    def get_queryset(self):
        user = self.request.user
        return WorkoutDetail.objects.filter(workout__user=user).order_by("-id")
    