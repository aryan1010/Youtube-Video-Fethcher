import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube_video_fetcher.settings")
os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")
app = Celery("youtube_video_fetcher")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
# app is the instance of Celery created above

# app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'


app.conf.beat_schedule = {
    "fetch_latest_videos": {
        "task": "videos.tasks.fetch_latest_videos",
        "schedule": crontab(minute="*/1"),  # Execute every minute
    },
}
