# part7

* install tmux, httpd , and mysql on yor machine
<<<<<<< HEAD
  > sudo yum -y install tmux
  > sudo yum -y install httpd
  > sudo yum -y install mysql

* create a folder "zabbix" for the rpm files
  > mkdir /var/www/html/zabbix

* Download the rpm files
  > wget --no-check-certificate https://repo.zabbix.com/zabbix/7.0/rhel/7/x86_64/zabbix-agent2-plugin-mongodb-7.0.0-release1.el7.x86_64.rpm -P /var/www/html/zabbix

* install createrepo
  > yum instal -y createrepo

* create a local repo
  > createrepo -v /var/www/html/zabbix
     
* Test the rpms from another vm and Apache server
 
=======
  > sudo yum -y install tmux httpd mysql

* create a local yum repo
  > yum-config-manager --add-repo="https://repo.zabbix.com/zabbix/7.0/rhel/7/x86_64/"

* Disable all other repos 
  > yum-config-manager --disable

* Install zabbix rpms 
  > yum install https://repo.zabbix.com/zabbix/7.0/rhel/7/x86_64/zabbix-release-latest.el7.noarch.rpm

>>>>>>> 7bdd5f742caed7b1afc206af2b6b5ad6edf6813c
