from googleapiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyDQbEU0T1sHPfTxh1ZDVt48wEBzek2N8hc'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_youtube_client():
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

def search_videos(client, query, max_results=50):
    response = client.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=max_results
    ).execute()

    videos = []
    for search_result in response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video = {
                'video_id': search_result['id']['videoId'],
                'title': search_result['snippet']['title'],
                'description': search_result['snippet']['description'],
                'published_at': search_result['snippet']['publishedAt'],
                'thumbnails': search_result['snippet']['thumbnails'],
            }
            videos.append(video)

    return videos