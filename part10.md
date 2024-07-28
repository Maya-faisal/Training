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
  > insert into students(id,firstName,lastName,program,gradYear)
  >  values(111100,'Dennis','Black','electrical',2020);
 
