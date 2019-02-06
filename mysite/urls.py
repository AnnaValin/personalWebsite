from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'portfolio', views.portfolio, name='portfolio'),
    url(r'blog', views.blog, name='blog'),
    url(r'contact', views.contact, name='contact'),
    url(r'index', views.index, name='index'),
    url(r'', views.index, name='index'),
]