from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator




class Meeting(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    start_time=models.DateTimeField(auto_now_add=False)
    end_time=models.DateTimeField(auto_now_add=False)
    # meeting_link=models.URLField(max_length=200)
    
    def __str__(self):
        return str(self.id)

