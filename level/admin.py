from django.contrib import admin

from level.models import Level


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('num', 'max_points')
    ordering = ('num',)
