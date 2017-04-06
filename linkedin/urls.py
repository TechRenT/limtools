from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^linkedin_form/$', views.linkedin_profile_create, name='linkedin_form'),
    url(r'^linkedin_list/$', views.linkedin_profile_list, name='linkedin_list'),
]