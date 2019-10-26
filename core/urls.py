from django.conf.urls import url

from core.views import SignUpView

app_name = 'core'

urlpatterns = [
    url(r'^api/signup/$', SignUpView.as_view(), name='signup'),
]
