from django.urls import path
from . import views

urlpatterns = [
    path('start-call/<int:to_user_id>/', views.start_or_go_video_call, name='start_call'),
    path('project/<int:project_id>/call/', views.video_call, name='video_call_jitsi'),
]