from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^seating', hello.views.seating),
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include('hello.urls'))
]
