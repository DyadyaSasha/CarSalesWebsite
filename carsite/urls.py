"""carsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import server_error, page_not_found, permission_denied
from django.utils.functional import curry


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'', include('cars.urls', namespace='cars')), 
]

handler403 = curry(permission_denied, exception=Exception('Permission Denied'), template_name='errs/403.html')
handler404 = curry(page_not_found, exception=Exception('Page not Found'), template_name='errs/404.html')
handler500 = curry(server_error, template_name='errs/500.html')

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
    ] + urlpatterns