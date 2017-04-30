from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^myadmin/$', views.admin_page, name='admin_page'),
    #url(r'^search/$', views.search, name='search'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^signin/$', views.signin, name='signin'),
    #url(r'^profile/$', vews.profile, name='profile'),
    url(r'^myadmin/users/$', views.list_of_users, name='listofusers'),
    url(r'^myadmin/add/$', views.add, name='add'),
    url(r'^myadmin/orders/$', views.orders, name='orders'),
    url(r'^myadmin/(?P<id>[0-9]+)/$', views.car_detail, name='car_detail'),
    url(r'^myadmin/delete/(?P<id>[0-9]+)/$', views.car_delete, name='car_delete'),
    url(r'^register/$', views.register, name='register'),
    url(r'^adminlogin/$', views.admin_login, name='admin_login'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^$', views.main_page, name='main_page'),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
