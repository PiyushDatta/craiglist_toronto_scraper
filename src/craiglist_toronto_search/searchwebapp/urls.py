from django.conf.urls import url
from . import views

urlpatterns = [
    # Start and end, our first/index page
    url(r'^$', views.index, name='index')
]