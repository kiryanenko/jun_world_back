from django.conf.urls import url

from level.views import AddLevelProgressView

app_name = 'level'

urlpatterns = [
    url(r'^progress/$', AddLevelProgressView.as_view(), name='add_level_progress'),
]
