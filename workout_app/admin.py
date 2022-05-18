from django.contrib import admin
from .models import (
    User,
    Workout,
    WorkoutDetail
)

admin.site.site_header = 'workout_app'
admin.site.register(User)
admin.site.register(Workout)
admin.site.register(WorkoutDetail)
