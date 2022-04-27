import mysql.connector
from getpass import getpass
from pandas import read_csv
from mysql.connector import connect, Error

create_DB_query = "CREATE DATABASE covid_tracker_DB"

#IMPORTANT(PLEASE READ): If you are trying to build a localhosted database use this code. Otherwise DO NOT run this file!
create_Student_table_query = """
CREATE TABLE Student(
	Sid INT PRIMARY KEY,
	Address VARCHAR(100)
)
"""
create_Residence_table_query = """
CREATE TABLE Residence(
	Address VARCHAR(100) PRIMARY KEY
)
"""
create_Section_table_query = """
CREATE TABLE Section(
	Cid INT PRIMARY KEY,
	inperson BIT
)
"""
create_Orgainzations_table_query = """
CREATE TABLE Organizations(
	Orgid INT PRIMARY KEY,
	inperson BIT,
	lastmeeting DATE
)
"""
create_Tests_table_query = """
CREATE TABLE Tests(
	Sid INT PRIMARY KEY,
	hascovid BIT,
	positivedate DATE
)
"""
create_Vaccination_table_query = """
CREATE TABLE Vaccination(
	Sid INT PRIMARY KEY,
	lastdosedate DATE,
	numdoses INT,
	dosetype VARCHAR(100)
)
"""
create_Livesin_table_query = """
CREATE TABLE LivesIn(
	Address VARCHAR(100),
	Sid INT,
	PRIMARY KEY (Address, Sid),
	FOREIGN KEY (Address) REFERENCES Residence(Address),
	FOREIGN KEY (Sid) REFERENCES Student(Sid)
)
"""
create_Enrolled_table_query = """
CREATE TABLE Enrolled(
	Cid INT,
	Sid INT,
	PRIMARY KEY (Cid, Sid),
	FOREIGN KEY (Cid) REFERENCES Section(Cid),
	FOREIGN KEY (Sid) REFERENCES Student(Sid)
)
"""
create_Participates_table_query = """
CREATE TABLE Participates(
	Orgid INT,
	Sid INT,
	PRIMARY KEY (Orgid, Sid),
	FOREIGN KEY (Orgid) REFERENCES Organizations(Orgid),
	FOREIGN Key (Sid) REFERENCES Student(Sid)
)
"""

# read in data from Kevin's generated data
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
"""
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
"""

try:
	with connect(
		host="localhost",
		user=input("Enter username: "),
		password=getpass("Enter password: "),
		#database="covid_tracker_DB"
	) as connection:
		with connection.cursor() as cursor:
			cursor.execute(create_DB_query)
			connection.commit()

			cursor.execute(create_Student_table_query)
			# Insert DataFrame to Table
			for row in df_stud.itertuples():
				cursor.execute('''
                INSERT INTO  Student(Sid, Address)
                VALUES (%s,%s)
                ''',
                row.sid,
                row.residence
                )
			cursor.commit()
		
			cursor.execute(create_Residence_table_query)
			# Insert DataFrame to Table
			for row in df_resid.itertuples():
				cursor.execute('''
                INSERT INTO Residence (Address)
                VALUES (%s)
                ''',
                row.residence
                )
			cursor.commit()
		
			cursor.execute(create_Section_table_query)
			# Insert DataFrame to Table
			for row in df_sect.itertuples():
				cursor.execute('''
                INSERT INTO Section (Cid, inperson)
                VALUES (%s,%s)
                ''',
                row.cid,
                row.in_person
                )
			cursor.commit()

			cursor.execute(create_Orgainzations_table_query)
			# Insert DataFrame to Table
			for row in df_org.itertuples():
				cursor.execute('''
                INSERT INTO Organizations (Orgid, inperson, lastmeeting)
                VALUES (%s, %s, %s)
                ''',
                row.orgid,
                row.in_person,
                row.last_meeting_day

                )
			cursor.commit()

			cursor.execute(create_Tests_table_query)
			# Insert DataFrame to Table
			for row in df_tests.itertuples():
				cursor.execute('''
                INSERT INTO Tests (Sid, hascovid, positivedate)
                VALUES (%s, %s, %s)
                ''',
                row.sid,
                row.has_covid,
                row.positive_date
                )
			cursor.commit()

			cursor.execute(create_Vaccination_table_query)
			# Insert DataFrame to Table
			for row in df_vax.itertuples():
				cursor.execute('''
                INSERT INTO Vaccination (Sid, lastdosedate, numdoses, dosetype)
                VALUES (%s, %s, %s, %s)
                ''',
                row.sid,
                row.last_dose_date,
                row.num_doses,
                row.dose_type
                )
			cursor.commit()

			cursor.execute(create_Livesin_table_query)
			# Insert DataFrame to Table
			for row in df_resid.itertuples():
				cursor.execute('''
                INSERT INTO Livesin (Address, Sid)
                VALUES (?,?)
                ''',
                #Make data for lives in table
                #row.sid,
                #row.cid
                )
			cursor.commit()

			cursor.execute(create_Enrolled_table_query)
			# Insert DataFrame to Table
			for row in df_enroll.itertuples():
				cursor.execute('''
                INSERT INTO Enrolled (Cid, Sid)
                VALUES (%s,%s)
                ''',
                row.cid,
                row.sid
                )
			cursor.commit()
		
			cursor.execute(create_Participates_table_query)
			# Insert DataFrame to Table
			for row in df_part.itertuples():
				cursor.execute('''
                INSERT INTO Participates (Orgid, Sid)
                VALUES (%s,%s)
                ''',
                row.orgid,
                row.sid
                )
			cursor.commit()

			connection.commit()
except Error as e:
	print(e)