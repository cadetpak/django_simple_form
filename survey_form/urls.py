from django.conf.urls import include, url 
from django.contrib import admin

urlpatterns = [
	url(r'^', include('apps.surveys.urls')),
    url(r'^admin/', admin.site.urls),
]
