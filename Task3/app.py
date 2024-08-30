#--------- imports ---------

import logging
from flask import Flask , render_template
import psutil
import shutil 
from functools import wraps
import datetime
import unittest
import mysql
import mysql.connector

# ---------- logger ---------

app = Flask(__name__)


logging.basicConfig(level=logging.INFO, filename="log.log" , filemode="w" , format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


#-------- Logs Function ------
def log_calls(fn):
    @wraps(fn)
    def wrapper(*args):
            logger.info(f"Calling Function: {fn.__name__} with args: {args}")
            result = fn(*args)
            logger.info(f" Function {fn.__name__} returned: {result}")
            return result
    return wrapper


#------- DataBase creation -------

@log_calls
def create_database_if_not_exists(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    except mysql.connector.Error as err:
        logger.error(f"Failed creating database: {err}")
        raise

@log_calls
def create_table(cursor):
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

def insert(cursor,item,total,free,used,timestamp):
     # Insert data into the table
     cursor.execute("""
         INSERT INTO stats (item, total, free, used, timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (item, total, free, used, timestamp))
	

@log_calls
def store(item, total, free, used, timestamp):
    conn = None 
 
    # Connect to MariaDB
    conn = mysql.connector.connect(
           user="root",
           password="123",
           host="db",
           port=3306,
       )

    cursor = conn.cursor()
    # Create the database if it does not exist
    create_database_if_not_exists(cursor, "task3")

    # Select the database
    conn.database = "task3"	


    try:  
        insert(cursor,item,total,free,used,timestamp)

        # Commit the transaction
        conn.commit()
        logger.info("Data inserted successfully into MariaDB.")
    except mysql.connector.Error as e:
        logger.error(f"Error inserting data into MariaDB, tables not found creating it : {e}")
        create_table(cursor)
        insert(cursor,item,total,free,used,timestamp)
    finally:
        # Close the connection
        if conn is not None:
            conn.close()

#--------- Get Current system statistics function --------
@log_calls
def getCurrent(val,item):
   
    data=""

    if item == "disk":
       total = val[0]
       used = val[1]
       free = val[2] 

       data = f" Total Disk = {total}GB , Used = {used}GB , and Free = {free}GB"
       store(item,total,free,used,str(datetime.datetime.now()))
    
    elif item == "cpu":
         data = str(val)
         data += "%"
         store(item,val,0,0,str(datetime.datetime.now()))

    else:
        total = val[0]
        used = val[1]
        free = val[2]

        data = f" Total Memory = {total}GB ,  Used = {used}GB,  Free = {free}GB" 
        store(item,total,free,used,str(datetime.datetime.now()))

 
    # Create HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>System Current Usage</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color:powderblue; text-align:center; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .usage {{ margin: 20px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>System Usage</h1>
            <div class="usage">
                <h2>{item} Current Usage</h2>
                <p>{data}</p>
            </div>
        </div>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(f"/flask_blog/templates/{item}current.html", "w") as file:
        file.write(html_content)
 

#--------- convert reading to human readable values -----------
@log_calls
def humanize_Mvalues(memory_info):
   
    total_memory = f"{memory_info.total / (1024 ** 3):.2f}"  # Convert bytes to GB and format to 2 decimal places
    used_memory = f"{memory_info.used / (1024 ** 3):.2f}"    # Convert bytes to GB and format to 2 decimal places
    free_memory = f"{memory_info.free / (1024 ** 3):.2f}"    # Convert bytes to GB and format to 2 decimal places

    results = (total_memory, used_memory, free_memory)  
    return results
    

@log_calls
def humanize_Dvalues(disk_info):
    total_disk = f"{disk_info.total / (1024 ** 3):.2f}"  # Convert bytes to GB
    free_disk = f"{disk_info.free / (1024 ** 3):.2f}"  # Convert bytes to GB
    used_disk = f"{disk_info.used / (1024 ** 3):.2f}"  # Convert bytes to GB

    results = (total_disk , used_disk, free_disk)
    return results


#-------- APIs ------------ 
@log_calls
@app.route('/')
def hello():
    logger.info(f" {__name__} Get APi sent successfully.")
    return ("success : hello world")

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

@log_calls
@app.route('/disk')
def disk():
    return render_template('disk.html')

@log_calls
@app.route('/diskCurrent')
def diskCurrent():
    disk_usage = shutil.disk_usage("/")
    getCurrent(humanize_Dvalues(disk_usage),"disk")
    return render_template('diskcurrent.html')

@log_calls
@app.route('/memory')
def memory():
    return render_template('memory.html')

@log_calls
@app.route('/memoryCurrent')
def currentmemory():
    memory_info = psutil.virtual_memory()
    getCurrent(humanize_Mvalues(memory_info),"memory")
    return render_template('memorycurrent.html')

#------ App config ------
if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SEND_FILE_MAX_AGE'] = 0 
    app.run(host='0.0.0.0', debug=True)

