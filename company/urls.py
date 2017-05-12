from django.conf.urls import url
from . import views

urlpatterns = [
    #/firma/
    url(r'^$', views.index, name='Firmalar Ana Sayfası'),
    #/firma/1
    url(r'^(?P<company_id>[0-9]+)$', views.detail, name='Firma Detay Sayfası'),
]
