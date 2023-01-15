cd /app
echo "----- Setting Everything ------ " 
gunicorn -b :5000 --reload --access-logfile - --error-logfile - app:app