from django.db import models

# Create your models here.









class StreamingPlatforms(models.Model):
    name =models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    



class WatchList(models.Model):
    title=  models.CharField(max_length=50)
    storyLine=models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamingPlatforms, on_delete=models.CASCADE, related_name="watchlist")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        