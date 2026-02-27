# Social Media API Deployment Guide (AWS EC2)

## 1) API Documentation Endpoints
After starting the app, documentation is available at:

- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`
- OpenAPI schema: `/api/schema/`

## 2) Local Production-Like Run

1. Create and activate virtual environment.
2. Install dependencies from `requirements.txt`.
3. Copy `.env.example` to `.env` and fill values.
4. Run:
   - `python manage.py migrate`
   - `python manage.py collectstatic --noinput`
   - `gunicorn social_media_api.wsgi:application --bind 0.0.0.0:8000`

## 3) EC2 Setup

On Ubuntu EC2:

1. Install packages:
   - `sudo apt update`
   - `sudo apt install -y python3-venv python3-pip nginx`
2. Clone repo into `/home/ubuntu/social_media_api`.
3. Create virtualenv and install `requirements.txt`.
4. Create `.env` from `.env.example`.
5. Apply migrations and collect static.

## 4) Gunicorn + Nginx

1. Copy `deploy/gunicorn.service` to `/etc/systemd/system/gunicorn.service`.
2. Reload and start service:
   - `sudo systemctl daemon-reload`
   - `sudo systemctl start gunicorn`
   - `sudo systemctl enable gunicorn`
3. Copy `deploy/nginx-social-media-api.conf` to `/etc/nginx/sites-available/social_media_api`.
4. Enable site and restart Nginx:
   - `sudo ln -s /etc/nginx/sites-available/social_media_api /etc/nginx/sites-enabled`
   - `sudo nginx -t`
   - `sudo systemctl restart nginx`

## 5) SSL

Use Certbot for HTTPS:

- `sudo apt install -y certbot python3-certbot-nginx`
- `sudo certbot --nginx -d your-domain.com`

## 6) Monitoring and Maintenance

- Check logs:
  - `sudo journalctl -u gunicorn -f`
  - `sudo tail -f /var/log/nginx/error.log`
- Keep dependencies updated regularly.
- Back up database before major releases.

## 7) Deployment Command

Use helper script:

- `bash deploy/ec2_deploy.sh`

Update all placeholder paths/domains before production use.
