from django.conf.urls import url

from core.views import SignUpView, SignInView

app_name = 'core'

urlpatterns = [
    url(r'^api/signup/$', SignUpView.as_view(), name='signup'),
    url(r'^api/signin/$', SignInView.as_view(), name='signin'),
]
