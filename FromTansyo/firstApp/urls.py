from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$',views.hello),
    url(r'^welcome2/$',views.welcome2),
    url(r'^select_cons/$',views.select_cons),
    url(r'^merit/$',views.merit),
]
