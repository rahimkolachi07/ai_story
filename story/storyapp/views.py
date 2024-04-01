# views.py
from django.http import JsonResponse
from .main import main_story

# views.py
import signal

def handle_timeout(signum, frame):
    raise TimeoutError("Request timed out")

def generate_story(request):
    # Set timeout limit (in seconds)
    timeout_limit = 180  # Adjust as needed

    # Set up signal handler for timeout
    signal.signal(signal.SIGALRM, handle_timeout)
    signal.alarm(timeout_limit)

    try:
        title = request.GET.get('title')
        lang = request.GET.get('lang')
        loc = request.GET.get('loc')
        pic = request.GET.get('pic')

        if title and lang and loc and pic:
            result = main_story(title, lang, loc, pic)
            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': 'Missing parameters'}, status=400)
    except TimeoutError:
        return JsonResponse({'error': 'Request timed out'}, status=500)
    finally:
        # Reset the alarm
        signal.alarm(0)

