from django.conf.urls import url

from achievement.views import GetAchievementView

app_name = 'achievement'

urlpatterns = [
    url(r'^(?P<slug>\w+)/get/$', GetAchievementView.as_view(), name='add_achievement'),
]
