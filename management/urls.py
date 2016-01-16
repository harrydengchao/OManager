from django.conf.urls import url
# -----------------------------------------
from management import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^demo/$', views.demo),
    url(r'^addserverfun/$', views.addserverfun),
    #url(r'^addapp/$', views.addapp),
    #url(r'^addhost/$', views.addhost),
    #url(r'^addmodule/$', views.addmodule),
]