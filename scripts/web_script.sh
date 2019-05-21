#!/usr/bin/env bash
#Скрипт автоматической установки apache, php и mysql на сервер debian
#Удаляем неиспользуемые зависимости
dpkg --purge `dpkg -l | grep '^rc' | awk '{print $2}'`
#Устанавливаем и запускаем apache
apt-get -y install apache2
invoke-rc.d apache2 stop
invoke-rc.d apache2 start
#Устанавливаем php и mysql
apt-get -y install php5 libapache2-mod-php5
apt-get -y install mysql-server
apt-get -y install phpmyadmin
ln -s /usr/share/phpmyadmin/ /var/www/html/pma
