#!/bin/sh
# Start the Flask app
flask run --host=0.0.0.0 &

# Start the Python script
python3 /flask_blog/saveTOdb.py &

# Start cron in the foreground
cron -f 

