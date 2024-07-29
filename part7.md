# part7

* install tmux, httpd , and mysql on yor machine
  > sudo yum -y install tmux httpd mysql

* create a local yum repo
  > yum-config-manager --add-repo="https://repo.zabbix.com/zabbix/7.0/rhel/7/x86_64/"

* Disable all other repos 
  > yum-config-manager --disable

* Install zabbix rpms 
  > yum install https://repo.zabbix.com/zabbix/7.0/rhel/7/x86_64/zabbix-release-latest.el7.noarch.rpm

