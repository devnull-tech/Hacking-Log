npm run tailwind-watch
python3 manage.py dumpdata hacklog.Log > logs_data.json
python3 manage.py loaddata logs_data.json