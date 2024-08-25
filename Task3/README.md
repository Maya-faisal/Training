# GET APIs <br/>
**6 APIs required, <br/>
 3 for the statistics for each hour in the last 24 hours, and was done using cronjobs to collect the data <br/>
 3 for current Memory/CPU/Disk usage, and was collected using Python modules**

  e.g
```python
@log_calls
@app.route('/cpu')
def cpu():
    return render_template('cpu.html')

@log_calls 
@app.route('/cpuCurrent') 
def cpuCurrent(): 
    cpu_usage = psutil.cpu_percent(interval=1) 
    getCurrent(cpu_usage,"cpu") 
    return render_template('cpucurrent.html') 
```
# Logging
**Logging is configured to write INFO level messages and above to a file named log.log. <br/>**

**A logger object is created using logging.getLogger(__name__). Additionally, a decorator is applied to functions to automatically log their calls and results.<br/>**

**The @wraps(fn) decorator ensures the wrapper retains the original function’s metadata.**

```python
logging.basicConfig(level=logging.INFO, filename="log.log" , filemode="w" , format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_calls(fn):
    @wraps(fn)
    def wrapper(*args):
            logger.info(f"Calling Function: {fn.__name__} with args: {args}")
            result = fn(*args)
            logger.info(f" Function {fn.__name__} returned: {result}")
            return result
    return wrapper
```

# Unit-Testing
**Three test were implemented<br/>**
**1. Test the Humanize value function, that converts the collected data to Human readable values<br/>**
**2. Test Database connection and Data Insertion<br/>**
**3. Test the Flask App routes<br/>**

```python
class ActivityTests(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()


    def test_humanize(self):
        test_info = TestInfo(total=10367352832, used=8186245120, free=2181107712)
        result_test = ('9.66', '7.62', '2.03')
        self.assertEqual(humanize_Mvalues(test_info), result_test)
    
    def test_insert_to_DB(self):
        store("memory",12,3.1,9.9,"2024-08-21 11:07:10.203109")

        # Connect to the database and check if the entry exists
        conn = mysql.connector.connect( user="root",
                                        password="123",
                                        host="localhost",
                                        port=3306,
                                        database="task3"
                                      )
        c = conn.cursor()
        c.execute("SELECT * FROM stats  WHERE item='memory' AND total=12 AND free=3.1 AND used=9.9;")
        added = c.fetchone()
        conn.close()

        self.assertIsNotNone(added, "Entry was not added to the database")
        

    def test_routes(self):
        tester = app.test_client(self)
        response = tester.get('/cpu')
        # Check if the status code is 200 (OK)
        self.assertIn(b'<title>CPU Usage</title>', response.data)
```

```python
 python3 unit_test.py -v 
```
```python
test_humanize (__main__.ActivityTests) ... ok
test_insert_to_DB (__main__.ActivityTests) ... ok
test_routes (__main__.ActivityTests) ... FAIL

```


# DataBase
**Maria DataBase was used to store the data**

 ```python
#------- DataBase creation -------

@log_calls
def store(item, total, free, used, timestamp):
    conn = None 
    try:
        # Connect to MariaDB
        conn = mysql.connector.connect(
            user="root",
            password="123",
            host="db",
            port=3306,
            database="task3"
        )
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stats (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item VARCHAR(255),
                total DOUBLE,
                free DOUBLE,
                used DOUBLE,
                timestamp VARCHAR(255)
            )
        """)

        # Insert data into the table
        cursor.execute("""
            INSERT INTO stats (item, total, free, used, timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (item, total, free, used, timestamp))

        # Commit the transaction
        conn.commit()
        logger.info("Data inserted successfully into MariaDB.")
    except mysql.connector.Error as e:
        logger.error(f"Error inserting data into MariaDB: {e}")
    finally:
        # Close the connection
        if conn is not None:
            conn.close()
```

 ```python
 mariadb -u root -p

MariaDB [task3]> select * from stats;
+----+--------+-------+------+------+----------------------------+
| id | item   | total | free | used | timestamp                  |
+----+--------+-------+------+------+----------------------------+
| 11 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 12 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 13 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 14 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 15 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 16 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 17 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 18 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 19 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 20 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 21 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 22 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 23 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 24 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 25 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
| 26 | memory |    12 |  3.1 |  9.9 | 2024-08-21 11:07:10.203109 |
+----+--------+-------+------+------+----------------------------+
16 rows in set (0.000 sec)

 ```

# Docker and Containerization
**1. First, create the Dockerfile for the Flask App** <br/>

  __install python base image__ <br/>
  __install all required modules__ <br/>
  __copy needed files and directories__ <br/> 
  __pass the environment variables for the Flask App__ <br/>
  __pass the CMD to run the flask app, bash and python scripts responsible for collecting data__ <br/>

**The start.sh script file starts the cronjobs and the flask App**<br/>

```bash
#!/bin/sh<br/>
#Start the Flask app<br/>
flask run --host=0.0.0.0 &<br/>
#Start cron in the foreground<br/>
cron -f<br/>
```

**2. Create the docker-compose file**<br/>

**Create the compose file that links the app with the database, and pass the database credentials.<br>
It builds the flask app image with tag v1 and host it on port 5000, mariadb image on port 3306, as "db" host.**

```yml
version: '3'
services:
  db:
    image: mariadb

    restart: always

    environment:
      MARIADB_USER: root
      MARIADB_ROOT_PASSWORD: 123
      MARIADB_DATABASE: task3

    networks:
      - my-network 
   
  v1:
    build: .

    ports:
      - "5000:5000"

    depends_on:
      - db

    networks:
      - my-network

networks:
  my-network:
    driver: bridge
```

# Pushing the Flask App Image to Docker HUB
 **First create a docker hub account, then log into it to push and follow these commands:** <br/>
 ```bash
 docker login 
 docker image tag yourtag username/reponame:imagetag
 docker push username/reponame:tag 
```

 # How to Pull the Image and use it
 
 **1. pull the image**

 ```bash
  docker pull 1maya1/training:v1
```

  > [!NOTE]
  > Make sure to have enough disk space, if not then enjoy doing a new partition for Docker data :)


**2. Make sure to have docker-compose installed, if not install it using this command**
  ```bash 
  curl -SL https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose 
  chmod +x /usr/local/bin/docker-compose
```

**3. Download the provided Docker-compose.yml and Dockerfile files and run the following command**
```bash
 docker-compose -d up
```

**4. Test the App using the GET APIs on port 5000**
```bash
http://127.0.0.1:5000/cpu 
http://127.0.0.1:5000/cpuCurrent
```

> [!NOTE]
> Make sure to add port 5000 to iptables and accept requests.
> Also, add port forwarding to your VM machine
