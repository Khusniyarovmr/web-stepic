sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo gunicorn -c /home/box/web/etc/gunicorn-conf.py hello:application
sudo gunicorn -c /home/box/web/etc/gunicorn-django-conf.py ask.wsgi:application
sudo /etc/init.d/mysql start
sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "create database stepic_web;"
#sudo mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
sudo mysql -uroot -e "create user 'box'@'localhost' identified by 'secret';"
sudo mysql -uroot -e "grant all priveleges on *.* to 'box'@'localhost' identified by 'secret' with grant option;"
sudo /home/box/web/ask/manage.py makemigrations
sudo /home/box/web/ask/manage.py migrate
