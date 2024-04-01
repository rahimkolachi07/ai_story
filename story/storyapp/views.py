# views.py
from django.http import JsonResponse
from storyapp.main import *

def generate_story(request):
    title = request.GET.get('title')
    lang = request.GET.get('lang')
    loc = request.GET.get('loc')
    pic = request.GET.get('pic')

    if title and lang and loc and pic:
        result = main_story(title, lang, loc, pic)
        return "done"
    else:
        return JsonResponse({'error': 'Missing parameters'}, status=400)
