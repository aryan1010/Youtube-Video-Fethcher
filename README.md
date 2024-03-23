- [x] Background Youtube API Call (through celery)
- [x] GET API which returns  data in a paginated response
- [x] Added support for supplying multiple API keys
- [x] Dashboard (through django admin)to view the stored videos with filters and sorting options
- [x] Meaningful variable/function names, and maintain indentation and code style
- [x] Each function commented for better understandability
- [x] Used DRF for creating APIs, celery for background task running, redis for brokerage  

# Installation:

Install Python and Redis from here https://github.com/tporadowski/redis/releases 

```python
pip install django djangorestframework celery redis google-api-python-client django-celery-beat
```

Clone the Repo
```
git clone 
```

Make migrations
```python
python manage.py migrate
```

Run the Celery worker:
```python
celery -A youtube_video_fetcher worker --loglevel=info 
```

Run  Celery Beat scheduler:
```python
celery -A youtube_video_fetcher beat --loglevel=info 
```

Start the Django  server:
```python
python manage.py runserver
```

Create a superuser
```python
python manage.py createsuperuser
```
# Usage:
## Get Videos API
```python
http://127.0.0.1:8000/api/videos/
```
## Add API key 
```python
http://127.0.0.1:8000/admin/videos/apikey/
```
## Dashboard [searching, sorting, filtering ]
Clone the Repo
```python
http://127.0.0.1:8000/admin/videos/video/
```

