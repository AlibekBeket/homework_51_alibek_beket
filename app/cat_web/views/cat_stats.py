from random import randint

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from cat_web.db import CatAction


def cat_stats_view(request: WSGIRequest):
    our_cat = CatAction('static/cat_status.json', request)
    our_cat.new_cat()
    our_cat.cat_action()
    our_cat.cat_stats_check()
    cat_status = our_cat.return_cat_dict()
    return render(request, 'cat_stats.html', context=cat_status)
