from django.conf.urls import url
# ------------------------------
from operations import views

urlpatterns = [
    url(r'^$', views.index),
 ]