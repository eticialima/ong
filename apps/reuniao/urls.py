from django.urls import path
from .views import request_meeting, manage_meetings, meeting_success

urlpatterns = [
    path('request-meeting/', request_meeting, name='request_meeting'),
    path('manage-meetings/', manage_meetings, name='manage_meetings'),
    path('meeting-success/', meeting_success, name='meeting_success'), 
]
