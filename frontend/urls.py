from django.urls import path
from .views import FrontView

urlpatterns = [
   path("end/", FrontView.as_view()),
]