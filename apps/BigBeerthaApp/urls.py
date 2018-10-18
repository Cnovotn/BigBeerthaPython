from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index)   # this says "any request sent to this route, have views.py handle the request.
]  