from django.conf.urls import include
from django.urls import path

from connect.views import connect_page

urlpatterns = [
    path('', connect_page),
]