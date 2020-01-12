from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$',views.hello),
    url(r'^welcome/$',views.welcome),
    url(r'^form_test/$',views.form_test),
]
