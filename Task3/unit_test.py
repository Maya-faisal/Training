import unittest
from app import *
from app import app
from flask import Flask, render_template
from collections import namedtuple
import mysql
import mysql.connector
import os

# Define the named tuple
TestInfo = namedtuple('TestInfo', ['total', 'used', 'free'])

app = Flask('flaskTest')

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

if __name__ == "__main__":
    unittest.main()
    
