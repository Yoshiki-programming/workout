from django.contrib import admin
from .models import (
    User,
    Workout,
    Weight,
    Sets,
    Reps
)

admin.site.site_header = 'workout_app'
admin.site.register(User)
admin.site.register(Workout)
admin.site.register(Weight)
admin.site.register(Sets)
admin.site.register(Reps)
