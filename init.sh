sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/gunicorn.conf.py
# sudo /etc/init.d/gunicorn restart
# gunicorn -w 2 -c /home/box/web/etc/hello.py hello:app
gunicorn -c /etc/gunicorn.d/gunicorn.conf.py hello:application &

# sudo /etc/init.d/mysql start