from django.shortcuts import render
from django.http import HttpResponse
from main import*


def my_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        lang = request.POST.get('lang')
        loc = request.POST.get('loc')
        pic = request.POST.get('pic')

        main_story(title, lang, loc, pic)

        return HttpResponse("done")
    else:
        # Return an error response for unsupported methods
        return HttpResponse("issue", status=405)
