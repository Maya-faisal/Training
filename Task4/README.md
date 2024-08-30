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
     
      services:
      db:
        image: bitnami/mariadb-galera
        container_name: node1
        environment:
          - ALLOW_EMPTY_PASSWORD= yes
          - MARIADB_GALERA_MARIABACKUP_PASSWORD=<password>
          - MARIADB_ROOT_PASSWORD=<password>
          - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes
          - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://
          - MARIADB_GALERA_NODE_ADDRESS=1<node1_ip>
          - MARIADB_GALERA_CLUSTER_NAME= galera_cluster
          - MARIADB_MASTER_HOST=<master_node_ip>
        restart: unless-stopped
        networks:
          - app-tier
        volumes:
          - /path/to/mariadb-persistence:/bitnami/mariadb
      
      v1:
        image: v1
        ports:
          - "5000:5000"
        depends_on:
          - db
        networks:
          - app-tier
      
      networks:
      app-tier:
        driver: bridge

  ```
- On the **second and third nodes**, modify the `docker-compose.yml` file accordingly:
 
  ```yaml
     services:
        db:
          image: bitnami/mariadb-galera
          container_name: node2
          environment:
            - ALLOW_EMPTY_PASSWORD= yes
            - MARIADB_GALERA_MARIABACKUP_PASSWORD= <password>
            - MARIADB_ROOT_PASSWORD= <password>
            - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://<bootstrap_node_ip>
            - MARIADB_GALERA_NODE_ADDRESS=<node2_ip>
            - MARIADB_GALERA_CLUSTER_NAME= galera_cluster
          restart: unless-stopped
          networks:
            - app-tier
          volumes:
            - /path/to/mariadb-persistence:/bitnami/mariadb
        
      networks:
        app-tier:
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

  > [!NOTE]
  > Make sure to open all necessary ports to enable communication between VMs
