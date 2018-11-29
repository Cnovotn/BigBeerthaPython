from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),   # this says "any request sent to this route, have views.py handle the request.
    url(r'^buyBeertha$', views.buyBeertha),
    url(r'^social$', views.socialPage),
    url(r'^contact$', views.contactPage),
    url(r'^addToCart$', views.addToCart),
    url(r'^viewCart$', views.viewCart),
    url(r'^checkout$', views.checkout)
] 