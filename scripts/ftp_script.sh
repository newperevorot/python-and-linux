#!/usr/bin/env bash
user="oleg"
group="webusers"

apt-get install vsftpd
cat /dev/null > /etc/vsftpd.conf
echo "listen=NO
listen_ipv6=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
chroot_local_user=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO" > /etc/vsftpd.conf

adduser $user
groupadd $group
mkdir -p /home/$user/www
mkdir -p /home/$user/logs

chown $user:$group /home/$user/www
chown $user:$group /home/$user/logs
chmod 555 /home/$user

/etc/init.d/vsftpd restart
