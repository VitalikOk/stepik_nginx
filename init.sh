sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx start
sudo rm -rf /etc/gunicorn.d/gunicorn.conf.py
sudo ln -s /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/gunicorn.conf.py
sudo mkdir -p /home/box/web/{log,pid}/
sudo touch /home/box/web/log/{gunicorn_access.log,gunicorn_error.log}
sudo touch /home/box/web/pid/gupid.pid
sudo gunicorn -c /etc/gunicorn.d/gunicorn.conf.py hello:application --bind 0.0.0.0:8080 &
sudo gunicorn -c /etc/gunicorn.d/gunicorn.conf.py ask/ask.wsgi:application --bind 0.0.0.0:8000 &
sudo /etc/init.d/mysql start  
mysql -uroot -e "create database stepik;"
mysql -uroot -e "create user 'stepik'@'localhost' identified by 'stepik;"
mysql -uroot -e "grant all privileges on  stepik.* to 'stepik'@'localhost'with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate
