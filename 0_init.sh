sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev    # скачиваем питон
sudo rm /usr/bin/python3     #sudo unlink /usr/bin/python3  
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo rm /usr/bin/python    #sudo unlink /usr/bin/python3  
sudo ln -s /usr/bin/python3.5 /usr/bin/python    # поставить на его место питон 3.5
sudo pip3 install gunicorn 
sudo pip3 install django==2.0
sudo pip3 install mysqlclient


   
# sudo pip3 install pymysql
# # sudo python3 -m pip install mysqlclient
# sudo pip3 install mysql-python


