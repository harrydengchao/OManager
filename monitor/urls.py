from django.conf.urls import url
# ------------------------------
from monitor import views
 urlpatterns = [
     url(r'^index/$', views.index),
 ]