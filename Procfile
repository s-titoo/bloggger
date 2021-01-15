web: flask db upgrade; flask translate compile; gunicorn bloggger:app
worker: rq worker -u $REDIS_URL bloggger-tasks
