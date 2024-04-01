# urls.py
from django.urls import path
from storyapp.views import generate_story

urlpatterns = [
    path('generate_story/', generate_story, name='generate_story'),
    # other paths...
]
