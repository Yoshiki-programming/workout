from django.contrib.auth import get_user_model
from rest_framework import generics
from workout_app.models import Workout, WorkoutDetail
from .serializers import WorkoutDetailSerializer, WorkoutSerializer, UserSerializer
User = get_user_model()
# Create your views here.

# ログインユーザーで筋トレメニューをpost、追加したメニューをgetできる
class WorkoutList(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    def get_queryset(self):
        user = self.request.user
        return Workout.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
# ユーザー制限かつポストできるようにする
class Recordlist(generics.ListCreateAPIView):
    queryset = WorkoutDetail.objects.all()
    serializer_class = WorkoutDetailSerializer

# class Recordlist(generics.RetrieveUpdateDestroyAPIView):
#     queryset = WorkoutDetail.objects.all()
#     serializer_class = WorkoutDetailSerializer