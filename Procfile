web: gunicorn run:app
release: pymongo-migrate migrate -u $(MONGODB_URI) -m migrations
