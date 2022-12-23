sudo apt -y update
sudo apt install -y python3.5
sudo apt install -y python3.5-dev   
sudo rm /usr/bin/python3      
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo rm /usr/bin/python    
sudo ln -s /usr/bin/python3.5 /usr/bin/python    
sudo pip3 install -y gunicorn 
sudo pip3 install -y django==2.0
sudo pip3 install -y mysqlclient


