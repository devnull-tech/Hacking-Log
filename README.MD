npm run tailwind-watch
python manage.py dumpdata hacklog.Log > data/logs_data.json
convert to utf8
python manage.py loaddata logs_data.json