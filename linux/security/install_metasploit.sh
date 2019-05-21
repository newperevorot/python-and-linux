#!/usr/bin/env bash
apt-get install curl
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod +x msfinstall
./msfinstall
msfupdate
rm -r ./msfinstall
#Запускаем программу msfconsole
