#!/flask_blog/bin/python3

import os
from functools import wraps
import logging
import mysql.connector
import datetime
from app import log_calls, store
from apscheduler.schedulers.blocking import BlockingScheduler

# Configure logging
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to store data and log the operation
def store_and_log(data_type, data, param1, param2, timestamp):
    try:
        store(data_type, data, param1, param2, timestamp)
        logger.info(f"Stored {data_type} data: {data}, {param1}, {param2}, {timestamp}")
    except Exception as e:
        logger.error(f"Failed to store {data_type} data: {e}")

def perform():
    for path, folders, files in os.walk("/flask_blog/templates/readings"):
        for filename in files:
           if 'cpu' in filename:
               with open(f"/flask_blog/templates/readings/{filename}") as f:
                    timedate = filename.split("_")
                    timestamp = f"{timedate[3]} {timedate[4]}"
                    store_and_log("cpu", f.read(), 0, 0, timestamp)

           elif 'memory' in filename:
                with open(f"/flask_blog/templates/readings/{filename}") as f:
                    timedate = filename.split("_")
                    timestamp = f"{timedate[3]} {timedate[4]}"
                    data = f.read()
                    data = data.replace('M', '').replace('G', '').replace('i','').replace('\n', '')
                    dataArr = data.split(" ")
                    total = float(dataArr[0]) + float(dataArr[1])
                    store_and_log("memory", total, dataArr[0], dataArr[1], timestamp)

           elif 'disk' in filename:
                with open(f"/flask_blog/templates/readings/{filename}") as f:
                     timedate = filename.split("_")
                     timestamp = f"{timedate[3]} {timedate[4]}"
                     data = f.readlines()
                     for line in data:
                         line = line.replace('M', '')
                         line = line.split(" ")
                         store_and_log(line[0], float(line[1])+float(line[2]), line[1], line[2], timestamp)


scheduler = BlockingScheduler()
scheduler.add_job(perform, 'interval', minutes=1)
scheduler.start()

