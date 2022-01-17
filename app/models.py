from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime




class Meeting(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    start_time=models.TimeField(auto_now_add=False)
    end_time=models.TimeField(auto_now_add=False)
    date=models.DateField(default=datetime.now())
    # meeting_link=models.URLField(max_length=200)
    
    def __str__(self):
        return str(self.id)

