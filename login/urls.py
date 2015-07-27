from django.conf.urls import include, url
from django.contrib import admin

from index import views as indexView
from IOT_Users import views as IOTView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', indexView.Login),
    url(r'^logout/$', indexView.Logout),
    url(r'^home/$', indexView.Home),
    url(r'^blog/$', indexView.Blog),
    url(r'^$', indexView.Home),
    url(r'^IOT/$', IOTView.home),
    url(r'^IOT/profile/$', IOTView.profile),
]