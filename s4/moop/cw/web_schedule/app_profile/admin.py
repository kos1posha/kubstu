from django.contrib import admin

from app_profile.models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'group_code']
