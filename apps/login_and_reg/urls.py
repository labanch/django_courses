# Inside your app's urls.py file
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success)
    # url(r'^(?P<course_id>\d+)/confirm$', views.confirm),
    # url(r'^(?P<course_id>\d+)/delete$', views.delete)
]
