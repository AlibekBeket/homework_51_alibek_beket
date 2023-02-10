from django.urls import path

from cat_web.views.cat_stats import cat_stats_view
from cat_web.views.new_cat import home_view

urlpatterns = [
    path('', home_view),
    path('cat_stats', cat_stats_view)
]
