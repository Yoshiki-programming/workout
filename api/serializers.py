from rest_framework import serializers
from django.contrib.auth import get_user_model
from workout_app.models import WorkoutDetail, Workout
User = get_user_model()
from logging import getLogger
logger = getLogger(__name__)

# 親モデル
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
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
            "id",
            "user",
            "part_of_body",
            "workout",
            "memo"
        ]

# 子モデル
class WorkoutDetailSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer(read_only=True)
    class Meta:
        model = WorkoutDetail
        fields = [
            "id",
            "workout",
            "workout_id",
            "weight",
            "reps",
            "date",
            "memo",
        ]
    def create(self, validated_data):
        validated_data['workout'] = validated_data.get('workout_id', None)
        
        if validated_data['workout'] is None:
            raise serializers.ValidationError("workout not found.") 

        del validated_data['workout_id']
        return WorkoutDetail.objects.create(**validated_data)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_workout = Workout.objects.filter(user=self._user)
        self.fields['workout_id'] = serializers.PrimaryKeyRelatedField(
            write_only=True,
            queryset=user_workout,
            default=user_workout)

    @property
    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.user

# 全ての結果ワークアウトの結果を可視化するページ
class MypageSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer(read_only=True)
    class Meta:
        model = WorkoutDetail
        fields = [
            "id",
            "workout",
            "weight",
            "reps",
            "date",
            "memo"
        ]