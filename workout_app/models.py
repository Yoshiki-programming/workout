from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
 

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
    def __str__(self):
        return self.username

class Workout(models.Model):
    user = models.ForeignKey(
        User,
        get_user_model(),
        verbose_name="ユーザー名",
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
    def __str__(self):
        return '%s: %s' % (self.part_of_body, self.workout)

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

    def __str__(self):
        return '%s: %s kg' % (self.workout, self.weight)