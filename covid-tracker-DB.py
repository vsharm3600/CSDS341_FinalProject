import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error

try:
	with connect(
    	host="localhost",
    	user=input("Enter username: "),
    	password=getpass("Enter password: "),
    	database="covid_tracker",
 	) as connection:
		print(connection)
except Error as e:
	print(e)