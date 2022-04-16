from asyncore import read
from rest_framework import serializers
from django.contrib.auth import get_user_model
from workout_app.models import WorkoutDetail, Workout
from rest_framework.serializers import SerializerMethodField
User = get_user_model()

# 親モデル
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "heights",
            "weights",
        ]
# ワークアウトを追加するためのシリアライザー
class WorkoutSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Workout
        fields = [
            "user",
            "part_of_body",
            "workout",
            "memo"
        ]

# 子モデル
class WorkoutDetailSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer()
    class Meta:
        model = WorkoutDetail
        fields = [
            "workout",
            "weight",
            "reps",
            "date",
            "memo"
        ]


