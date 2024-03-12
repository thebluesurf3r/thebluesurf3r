from django.db import models

class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics')  # Optional upload path
