from celery import shared_task
from .youtube import get_youtube_client, search_videos
from .models import Video

SEARCH_QUERY = 'Cricket'

@shared_task
def fetch_latest_videos():
    youtube_client = get_youtube_client()
    videos = search_videos(youtube_client, SEARCH_QUERY)

    for video in videos:
        Video.objects.update_or_create(
            video_id=video['video_id'],
            defaults={
                'title': video['title'],
                'description': video['description'],
                'published_at': video['published_at'],
                'thumbnails': video['thumbnails'],
            }
        )