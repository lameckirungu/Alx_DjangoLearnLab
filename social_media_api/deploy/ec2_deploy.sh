#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/home/ubuntu/social_media_api"
cd "$APP_DIR"

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate --noinput
python manage.py collectstatic --noinput

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo systemctl enable gunicorn
sudo systemctl enable nginx

echo "Deployment complete."
