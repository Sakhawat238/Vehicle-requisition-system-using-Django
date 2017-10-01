
from django.conf.urls import url
from . import views

urlpatterns = [
    # home/
    url(r'^$', views.home, name="homepage"),

    # home2
    url(r'^home2/$', views.home2, name="loghome"),
    # home/register/
    url(r'^register/$', views.register, name="reg"),

    # home/login
    url(r'^login/$', views.login_user, name="log"),

    # home/logout
    url(r'^logout/$', views.logout_user, name='out'),

    # home/cars
    url(r'^vehicles/$', views.showcar, name='caaar'),

    # home/rent
    url(r'^rent/$', views.create_rentdata, name='rnt'),

    # home/confirmation
    url(r'^confirm/$', views.confirmation, name='conf'),

    # home/faq
    url(r'^faq/$', views.faq, name='fq')

]
