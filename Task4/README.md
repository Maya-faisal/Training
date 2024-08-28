# High availability cluster for MariaDB

**Setting up a 3-node MariaDB Galera cluster for high availability, for Task3 image.**

Here are the steps to set up a 3-node Galera cluster with MariaDB using containers, each on a separate VM:

1. **Create 3 VMs Connected via NAT Network**
- Ensure all VMs are configured to use a NAT network for internal communication.

2. **Check IP Addresses and Test Connectivity**
- Identify the IP address of each VM.
- Use the `ping` command to verify that all VMs can communicate with each other.

3. **Update the `docker-compose.yml` File**
- On the **first node**, configure the `docker-compose.yml` file as follows:
     ```yaml
      version: '3'

      services:
        db:
          image: mariadb:latest
          environment:
            MYSQL_ROOT_PASSWORD: root_password
            MYSQL_DATABASE: example_db
            MYSQL_USER: example_user
            MYSQL_PASSWORD: user_password
            CLUSTER_NAME: "galera_cluster"
            CLUSTER_JOIN: ""  # First node, so no join address
          ports:
            - "3306:3306"
            - "4567:4567"
            - "4568:4568"
            - "4444:4444"
          volumes:
            - db_data:/var/lib/mysql
          networks:
            - galera_net
      
      v1:
         image: 1maya1/training:v1
         ports:
           - "5000:5000"
         depends_on:
           - db
         networks:
           - my-network
           
      volumes:
        db_data:
      
      networks:
        galera_net:
          driver: bridge
     ```
- On the **second and third nodes**, modify the `docker-compose.yml` file accordingly:
     ```yaml
     version: '3'

       services:
         mariadb:
           image: mariadb:latest
           environment:
             MYSQL_ROOT_PASSWORD: root_password
             MYSQL_DATABASE: example_db
             MYSQL_USER: example_user
             MYSQL_PASSWORD: user_password
             CLUSTER_NAME: "galera_cluster"
             CLUSTER_JOIN: "10.0.2.15"  # Join the cluster using Node 1's IP
           ports:
             - "3306:3306"
             - "4567:4567"
             - "4568:4568"
             - "4444:4444"
           volumes:
             - db_data:/var/lib/mysql
           networks:
             - galera_net
       
       volumes:
         db_data:
       
       networks:
         galera_net:
           driver: bridge
     ```

4. **Bootstrap the Cluster from Node 1**
- Start the Docker container on the first node to initialize the Galera cluster.
```bash
   docker-compose up -d
```

5. **Add Other VMs to the Cluster**
- Start the Docker containers on the second and third nodes to join them to the cluster.
```bash
   docker-compose up -d
```

6. **Verify the Cluster Size**
- Check the cluster size to confirm that all nodes are correctly added and operational.
```bash
   docker exec -it <container_name> mysql -u root -p
   SHOW STATUS LIKE 'wsrep_cluster_size';
```