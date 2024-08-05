# part10

* install mariadb mariadb-server 
  > 

* Enable and start MariaDB 
  > systemctl enable mariadb
  > systemctl start mariadb
  > sudo mysql_secure_installation

* open Maria DB port in iptables
  > iptables -I INPUT -p tcp --dport 3306 -j ACCEPT

* open an interactive MariaDB session as root 
  > mysql -u root -p

* create a new database "studentdb"
  > create database studentdb
  > use studentdb

* create a new table "students" 
  > create table students (id int primary key, firstName varchar(100) not null , lastName varchar(100) not null , program varchar(50) not null, gradYear int)

* insert data
  > insert into students(id,firstName,lastName,program,gradYear) <br />
  >  values(111100,'Dennis','Black','electrical',2020);

* view table
  
  ![image](https://github.com/user-attachments/assets/90922d31-4e51-4006-a911-68728284c6b4)

 
**To make queries remotely we need to dp the following**
<br />
* create a new user 
  > CREATE USER 'maya'@'localhost' IDENTIFIED BY '123';

* Grant remote privileges with GRANT
  > GRANT ALL PRIVILEGES ON *.* TO 'maya'@'10.10.10.57' IDENTIFIED BY '123'
