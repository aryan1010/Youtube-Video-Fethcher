from django.db import models


class Video(models.Model):
    """
    Model representing a video fetched from YouTube.
    """
    video_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnails = models.JSONField()

    def __str__(self):
        return self.title


class APIKey(models.Model):
    """
    Model representing a YouTube API key.
    """
    key = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.key
