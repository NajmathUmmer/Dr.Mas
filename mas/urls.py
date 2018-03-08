from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
	
	url(r'^drmas/$', views.home, name='home'),
    url(r'^login$', views.login_user, name='login_user'),
	url(r'^$', views.home, name='home'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^accept/$', views.accept, name='accept'),
	]
