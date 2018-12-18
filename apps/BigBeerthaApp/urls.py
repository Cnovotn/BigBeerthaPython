from django.conf.urls import url
from . import views     
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^buyBeertha$', views.buyBeertha),
    url(r'^social$', views.socialPage),
    url(r'^contentSubmission$', views.contentSubmission),
    url(r'^contact$', views.contactPage),
    url(r'^addToCart$', views.addToCart),
    url(r'^viewCart$', views.viewCart),
    url(r'^emptyCart$', views.emptyCart),
    url(r'^checkout$', views.checkout)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)