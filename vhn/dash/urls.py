from django.conf.urls import patterns, url

from dash import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^$', views.login, name='login'),
)
