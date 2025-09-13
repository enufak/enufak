from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=255)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_projects")
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="freelancer_projects")
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectCallRoom(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="call_room")
    room_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
