# Configuring Galera cluster with MariaDB using 3 nodes.

1. Configure your first Galera node. Each node in the cluster needs to have a nearly identical configuration. Because of this, you will do all of the configuration on your first machine, and then copy it to the other nodes.

```bash
sudo vi /etc/my.cnf.d/galera.cnf
```

2. Add the following configurations

```bash
[mysqld]
binlog_format=ROW
default-storage-engine=innodb
innodb_autoinc_lock_mode=2
bind-address=0.0.0.0

# Galera Provider Configuration
wsrep_on=ON
wsrep_provider=/usr/lib64/galera-4/libgalera_smm.so

# Galera Cluster Configuration
wsrep_cluster_name="galera_cluster"
wsrep_cluster_address="gcomm://First_Node_IP,Second_Node_IP,Third_Node_IP"

# Galera Synchronization Configuration
wsrep_sst_method=rsync

# Galera Node Configuration
wsrep_node_address="This_Node_IP"
wsrep_node_name="This_Node_Name"
```

4. Configure the remaining two nodes, by changing the following parts
```bash

wsrep_node_address="This_Node_IP"
wsrep_node_name="This_Node_Name"
```
5. Edit firewall and selinux policy

```bash
sudo firewall-cmd --permanent --zone=public --add-port=3306/tcp
sudo firewall-cmd --permanent --zone=public --add-port=4567/tcp
sudo firewall-cmd --permanent --zone=public --add-port=4568/tcp
sudo firewall-cmd --permanent --zone=public --add-port=4444/tcp
sudo firewall-cmd --permanent --zone=public --add-port=4567/udp
sudo firewall-cmd --permanent --zone=public --add-source=galera-node-1-ip/32
sudo firewall-cmd --permanent --zone=public --add-source=galera-node-2-ip/32
sudo firewall-cmd --permanent --zone=public --add-source=galera-node-3-ip/32

sudo semanage port -a -t mysqld_port_t -p tcp 4567
sudo semanage port -a -t mysqld_port_t -p udp 4567
sudo semanage port -a -t mysqld_port_t -p tcp 4568
sudo semanage port -a -t mysqld_port_t -p tcp 4444
sudo semanage permissive -a mysqld_t

```
6. stop the database server on all the nodes so that you will be able to bootstrap the database cluster with shared SELinux policies
```bash
systemctl stop mariadb
```

7.bootstrap the cluster to generate inter-node communication events
```bash
sudo galera_new_cluster
```

8. Create a test database on the first node
```bash
 mariadb -u root -p 
 create database task4;
 use task4;
 CREATE TABLE test (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
 ```
9. Bring the other nodes and check the database from it
```bash
systemctl start mariadb
mariadb -u root -p
use task4;
select * from test;
```
