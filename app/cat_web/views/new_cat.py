from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def home_view(request: WSGIRequest):
    return render(request, 'new_cat_page.html')
