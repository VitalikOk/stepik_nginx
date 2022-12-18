sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev    # скачиваем питон
sudo rm /usr/bin/python3     #sudo unlink /usr/bin/python3  
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo rm /usr/bin/python    #sudo unlink /usr/bin/python3  
sudo ln -s /usr/bin/python3.5 /usr/bin/python    # поставить на его место питон 3.5

sudo python3 -m pip install gunicorn #sudo pip3 install gunicorn      # установить жуникорн
sudo python3 -m install django==2.1 #sudo pip3 install django==2.1  
# sudo python3 -m pip install mysqlclient

sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-pil python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev


   
# sudo pip3 install pymysql
# # sudo python3 -m pip install mysqlclient
# sudo pip3 install mysql-python


