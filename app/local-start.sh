GUNICORN_CMD_ARGS="--bind=0.0.0.0:7002 --workers=1 --log-file=-" gunicorn app.app:app -e PYTHONUNBUFFERED=true -e LOCAL=true