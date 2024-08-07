# part7

* install tmux, httpd , and mysql on your machine
  > sudo yum -y install tmux httpd mysql

* create a folder "zabbix" for the rpm files
  > mkdir /var/www/html/zabbix

* Download the rpm files
  > wget --no-check-certificate https://repo.zabbix.com/zabbix/7.0/rhel/7/x86_64/zabbix-agent2-plugin-mongodb-7.0.0-release1.el7.x86_64.rpm -P /var/www/html/zabbix

* install createrepo
  > yum install -y createrepo

* create a local repo
  > createrepo -v /var/www/html/zabbix

* Disable all other repos, and try to install a rpm file from the new local repo
  > yum install zabbix-agent.x86_64 --disablerepo=* --enablerepo=zabbix
  
<br />   

* Test the rpms from another vm and Apache server <br /> <br/>
  **over http for Apache server, edit the /etc/yum.repos.d/zabbix.repo file as following**
   
     ![image](https://github.com/user-attachments/assets/d87b908c-5d60-4352-93fc-918b73238a4c)

  <br />

     ![image](https://github.com/user-attachments/assets/25c8c273-4464-4358-bfed-376930902c3f)

  
  **locally**
  
   ![image](https://github.com/user-attachments/assets/a0e83bdd-2967-4a35-b589-23b9c6d699ae)








