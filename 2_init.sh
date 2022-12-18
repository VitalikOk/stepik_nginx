
sudo /etc/init.d/mysql start  
mysql -uroot -e "create database stepik;"
mysql -uroot -e "create user 'stepik'@'localhost' identified by 'stepik';"
mysql -uroot -e "grant all privileges on  stepik.* to 'stepik'@'localhost'with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate
