# Generated by Django 4.0.4 on 2022-05-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0005_remove_workoutdetail_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutdetail',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='日付'),
        ),
    ]