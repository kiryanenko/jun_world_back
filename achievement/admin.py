from django.contrib import admin

# Register your models here.
from achievement.models import Achievement


@admin.register(Achievement)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('slug', 'points')
    fields = ('slug', 'points')