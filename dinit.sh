#!/bin/bash
apt-get install -y --force-yes libmysqlclient-dev
rm -rf /etc/nginx/sites-enabled/default
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
/etc/init.d/nginx start
# /etc/init.d/nginx restart
rm -rf /etc/gunicorn.d/gunicorn.conf.py
mkdir -p /etc/gunicorn.d
ln -s /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/gunicorn.conf.py
mkdir -p /home/box/web/{log,pid}/
touch /home/box/web/log/{gunicorn_access.log,gunicorn_error.log}
touch /home/box/web/pid/gupid.pid
gunicorn -c /etc/gunicorn.d/gunicorn.conf.py hello:application --bind 0.0.0.0:8080 &
cd /home/box/web/ask
gunicorn -c /etc/gunicorn.d/gunicorn.conf.py ask.wsgi:application --bind 0.0.0.0:8000 &
# /etc/init.d/mysql start  
mysql -uroot -e "create database stepik;"
mysql -uroot -e "create user 'stepik' identified by 'stepik';"
mysql -uroot -e "grant all privileges on *.* to 'stepik' with grant option;"

python3 /home/box/web/ask/manage.py makemigrations qa
python3 /home/box/web/ask/manage.py migrate

