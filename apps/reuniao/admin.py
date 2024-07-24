from django.contrib import admin
from .models import MeetingRequest

class MeetingRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'requested_at', 'status')
    list_filter = ('status', 'requested_at', 'user')
    search_fields = ('subject', 'description', 'user__username')
    ordering = ('-requested_at',)

admin.site.register(MeetingRequest, MeetingRequestAdmin)
