from django.conf.urls import url

from hello.views import UsersList

urlpatterns = [
    url(r'^users/$', UsersList.as_view(), name='users')
]