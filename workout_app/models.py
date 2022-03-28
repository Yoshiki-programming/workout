from django.db import models
from django.contrib.auth.models import AbstractUser
 

class User(AbstractUser):
    heights = models.FloatField(
        verbose_name="身長",
        blank=True,
        null=True,
        default=0
        )
    weights = models.FloatField(
        verbose_name="体重",
        blank=True,
        null=True,
        default=0
        )

class Workout(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="ユーザー名",
        on_delete=models.CASCADE,
        )
    part_of_body = models.CharField(
        verbose_name="部位",
        max_length=20
        )
    workout = models.TextField(
        verbose_name="ワークアウト名",
        )
    memo = models.TextField(
        verbose_name="メモ",
        blank=True,
        null=True,
        )

class WorkoutDetail(models.Model):
    workout = models.ForeignKey(
        Workout,
        verbose_name="ワークアウト",
        on_delete=models.CASCADE,
        )
    weight = models.FloatField(
        verbose_name="重さ",
        blank=True,
        null=True,
        )
    reps = models.IntegerField(
        verbose_name="回数",
        blank=True,
        null=True,
        )
    date = models.DateField(
        verbose_name="日付",
        blank=True,
        null=True,
        )
    memo = models.TextField(
        verbose_name="メモ",
        blank=True,
        null=True,
        )