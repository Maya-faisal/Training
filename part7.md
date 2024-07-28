# part7

* install tmux, httpd , and mysql on yor machine
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
 
