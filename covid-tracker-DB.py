import mysql.connector
from pandas import read_csv

from getpass import getpass
from mysql.connector import connect, Error

try:
	with connect(
    	host="localhost",
    	user=input("Enter username: "),
    	password=getpass("Enter password: ")
 	) as connection:
		print(connection)
except Error as e:
	print(e)


df_enroll = read_csv('Data/enrolled.csv')
df_org = read_csv('Data/organizations.csv')
df_part = read_csv('Data/participates.csv')
df_resid = read_csv('Data/residences.csv')
df_sect = read_csv('Data/section.csv')
df_stud = read_csv('Data/student.csv')
df_tests = read_csv('Data/tests.csv')
df_vax = read_csv('Data/vaccination.csv')

data = df_stud.values
print(data)

# TODO: SWAP OUT the X's
# first two are cursors, last one is connection
# Create Table
X.execute('''
		CREATE TABLE products (
			sid int primary key,
			cid int
			)
               ''')

# Insert DataFrame to Table
for row in df_enroll.itertuples():
    X.execute('''
                INSERT INTO products (sid, cid)
                VALUES (?,?)
                ''',
                row.sid,
                row.cid
                )
X.commit()
