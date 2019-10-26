from django.conf.urls import url

from core.views import SignUpView, SignInView, CurrentUserView

app_name = 'core'

urlpatterns = [
    url(r'^api/signup/$', SignUpView.as_view(), name='signup'),
    url(r'^api/signin/$', SignInView.as_view(), name='signin'),
    url(r'^api/users/me/$', CurrentUserView.as_view(), name='current_user'),
]
