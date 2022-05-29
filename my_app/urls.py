from django.conf.urls import url
from my_app import views

app_name = 'my_app'

urlpatterns = [
    url(r'^intra_in_cont/$', views.user_login, name="intra_in_cont"),
    url(r'^pag_loc/(?P<pk>\d+)/$', views.pag_places, name="pag_places"),
    url(r'^desk_availability/(?P<pk>\d+)/$', views.desk_availability, name="desk_availability"),
]