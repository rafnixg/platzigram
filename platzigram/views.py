"""Platzigram Views."""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime


def hello_world(request):
    """Return hello world."""
    return HttpResponse('Hello Word! the server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integer(request):
    """Return a list of sorted integer."""
    # import pdb; pdb.set_trace()
    res = {}
    res['numbers'] = sorted(map(int, request.GET['numbers'].split(',')))
    return JsonResponse(res)
