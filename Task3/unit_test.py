import unittest
from flaskTest import *
from flask import Flask, render_template
from collections import namedtuple
import sqlite3
import os

# Define the named tuple
TestInfo = namedtuple('TestInfo', ['total', 'used', 'free'])

app = Flask('flaskTest')

class ActivityTests(unittest.TestCase):
    def test_humanize(self):
        test_info = TestInfo(total=10367352832, used=8186245120, free=2181107712)
        result_test = ('9.66', '7.62', '2.03')
        self.assertEqual(humanize_Mvalues(test_info), result_test)

    def test_create_table(self):
        # Call the function to create the table
        create_table()

        # Connect to the database and check if the table exists
        conn = sqlite3.connect("task3.db", check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stats';")
        table_exists = c.fetchone()
        conn.close()

        # Assert that the table was created
        self.assertIsNotNone(table_exists, "Table 'stats' should exist")

    def TestInsertingToDB(self):
        store("memory",12,3.1,9.9,"2024-08-21 11:07:10.203109")

        # Connect to the database and check if the entry exists
        conn = sqlite3.connect("task3.db", check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT * FROM stats  WHERE item='memory' AND total=12 AND free=3.1 AND used=9.9;")
        added = x.fetchone()
        conn.close()

        self.assertIsNotNone(added, "Entry was not added to the database")


if __name__ == "__main__":
    unittest.main()

