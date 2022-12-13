sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo rm -rf /home/box/web/etc/*
sudo ln -s /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart
# gunicorn -w 2 -c /home/box/web/etc/hello.py hello:app
gunicorn -c /etc/gunicorn.d/test/gunicorn.conf.py hello

# sudo /etc/init.d/mysql start