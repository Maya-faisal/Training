#!/bin/sh
# Start the Flask app
flask run --host=0.0.0.0 &

# Start cron in the foreground
cron -f 

