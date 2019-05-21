#Установка значений
SITE_NAME=$1
HOST_PATH="/etc/apache2/vhosts"
DATABASE_NAME=$SITE_NAME
USERNAME="oleg"
PASSWORD="hs,fkrf"

#
cd /var/www/
mkdir $1
cd $1
wget https://ru.wordpress.org/latest-ru_RU.zip
unzip latest-ru_RU.zip
sudo rm -r latest-ru_RU.zip
mv wordpress/* .
sudo rm -r wordpress
sed "s/database_name_here/$DATABASE_NAME/g" wp-config-sample.php > wp-config-sample1.php
sed "s/username_here/$USERNAME/g" wp-config-sample1.php > wp-config-sample2.php
sed "s/password_here/$PASSWORD/g" wp-config-sample2.php > wp-config.php
sudo rm -r wp-config-sample*
cp /var/library/robots.txt ./robots_tmp.txt
cp /var/library/.htaccess .
sed "s/vseuznaem.su/$SITE_NAME/g" robots_tmp.txt > robots.txt
sudo rm -r robots_tmp.txt

#
mysql -uroot -phs,fkrf1987 -e "create database \`$DATABASE_NAME\`"
mysql -uroot -phs,fkrf1987 -e "grant all privileges on \`$DATABASE_NAME\`.* to '$USERNAME'@'localhost'";

#
ls
cd wp-content/themes/
cp /var/library/themes/basic.tar.gz .
tar -xzf basic.tar.gz
sudo rm -r basic.tar.gz

cd ../../../
cd $HOST_PATH
sudo cp /var/library/vhost.txt .
sudo sed "s/site/$SITE_NAME/g" vhost.txt > $SITE_NAME
sudo rm -r vhost.txt

mysql -u$USERNAME -p$PASSWORD $SITE_NAME < /var/library/wp.sql
echo $SITE_NAME
