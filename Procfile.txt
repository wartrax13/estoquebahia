release: python manage.py migrate --noinput
web: gunicorn projeto.wsgi --log-file -