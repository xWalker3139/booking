"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "my_app"

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'my_app/', include("my_app.urls", namespace='my_app')),
    url(r'^acasa/$', views.HomeView.as_view(), name="home"),
    url(r'contact/$', views.contact, name="contact"),
    url(r'^inregistrare/$', views.inregistrare, name="inregistrare"),
    url(r'^logout_user/$', views.logout_user, name="logout_user"),
    url(r'^contul_meu/(?P<pk>\d+)/$', views.contul_meu, name="contul_meu"),
    url(r'^birouri/$', views.all_desk, name="all_desk"),
    url(r'^cautare_birouri/$', views.cautare_birouri, name="cautare_birouri"),
    url(r'^pag_birouri/(?P<pk>\d+)/$', views.pag_desk, name="pag_desk"),
    url(r'^desk_availability/(?P<pk>\d+)/$', views.desk_availability, name="desk_availability"),
    url(r'^editeaza_profil/(?P<pk>\d+)/$', views.editeaza_profil, name="editeaza_profil"),
    url(r'^intrebari/$', views.intrebari, name="intrebari"),
    url(r'^cautare_birouri/(?P<pk>\d+)/$', views.search_places, name="search_places"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
