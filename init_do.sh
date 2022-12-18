# sudo apt update                     # готовимся скачивать питон
# sudo apt install python3.6          # скачиваем питон
# sudo rm /usr/bin/python3                         # удалить питон 3.4.3 из системы
# sudo ln -s /usr/bin/python3.6 /usr/bin/python3   # поставить на его место питон 3.5
# sudo pip3 install gunicorn      # установить жуникорн
# sudo pip3 install django==2.1     

sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m install django==2.0
sudo python3 -m pip install mysqlclient