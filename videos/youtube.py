from googleapiclient.discovery import build
from .models import APIKey

# YOUTUBE_API_KEY = 'AIzaSyDQbEU0T1sHPfTxh1ZDVt48wEBzek2N8hc'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_youtube_client():
    active_keys = APIKey.objects.filter(is_active=True)
    for key in active_keys:
        try:
            client = build(
                YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=key.key
            )
            return client
        except Exception as e:
            print(f"Error with API key {key.key}: {e}")
            key.is_active = False
            key.save()
    raise Exception("No available API keys found.")
    return build(
        YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY
    )


from datetime import datetime, timedelta


def search_videos(client, query, max_results=50):
    # Get the datetime for 24 hours ago
    published_after = datetime.utcnow() - timedelta(hours=1)
    published_after = published_after.isoformat() + "Z"

    response = (
        client.search()
        .list(
            q=query,
            type="video",
            part="id,snippet",
            maxResults=max_results,
            order="date",
            publishedAfter=published_after,
        )
        .execute()
    )

    videos = []
    for search_result in response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video = {
                "video_id": search_result["id"]["videoId"],
                "title": search_result["snippet"]["title"],
                "description": search_result["snippet"]["description"],
                "published_at": search_result["snippet"]["publishedAt"],
                "thumbnails": search_result["snippet"]["thumbnails"],
            }
            videos.append(video)

    return videos
