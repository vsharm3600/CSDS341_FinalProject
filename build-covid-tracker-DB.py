import mysql.connector
from getpass import getpass
from pandas import read_csv
from mysql.connector import connect, Error

create_DB_query = "CREATE DATABASE covid_tracker_DB"

#IMPORTANT(PLEASE READ): If you are trying to build a localhosted database use this code. Otherwise DO NOT run this file!
create_Student_table_query = """
CREATE TABLE Students(
	sid INT PRIMARY KEY,
	Address VARCHAR(100)
)
"""

create_Section_table_query = """
CREATE TABLE Section(
	cid INT PRIMARY KEY,
	inperson BIT
)
"""
create_Orgainzations_table_query = """
CREATE TABLE Organizations(
	orgid INT PRIMARY KEY,
	inperson BIT,
	lastmeeting DATE
)
"""
create_Tests_table_query = """
CREATE TABLE Tests(
	sid INT PRIMARY KEY,
	hascovid BIT,
	positivedate DATE
)
"""
create_Vaccination_table_query = """
CREATE TABLE Vaccination(
	sid INT PRIMARY KEY,
	lastdosedate DATE,
	numdoses INT,
	dosetype VARCHAR(100)
)
"""

create_Enrolled_table_query = """
CREATE TABLE Enrolled(
	cid INT,
	sid INT,
	PRIMARY KEY (cid, sid),
	FOREIGN KEY (cid) REFERENCES Section(cid),
	FOREIGN KEY (sid) REFERENCES Student(sid)
)
"""
create_Participates_table_query = """
CREATE TABLE Participates(
	orgid INT,
	sid INT,
	PRIMARY KEY (orgid, sid),
	FOREIGN KEY (orgid) REFERENCES Organizations(orgid),
	FOREIGN Key (sid) REFERENCES Student(sid)
)
"""

# read in data from Kevin's generated data
df_enroll = read_csv('Data/enrolled.csv')
df_org = read_csv('Data/organizations.csv')
df_part = read_csv('Data/participates.csv')
df_sect = read_csv('Data/section.csv')
df_stud = read_csv('Data/student.csv')
df_tests = read_csv('Data/tests.csv')
df_vax = read_csv('Data/vaccination.csv')

#old insertion queries that are not used
insert_student_records = '''
                INSERT INTO  Student (Sid, Address)
                VALUES (%s,%s)
                '''

insert_section_records = '''
                INSERT INTO Section (Cid, inperson)
                VALUES (%s,%s)
                '''

insert_organization_records = '''
                INSERT INTO Organizations (Orgid, inperson, lastmeeting)
                VALUES (%s, %s, %s)
                '''

insert_tests_records = '''
                INSERT INTO Tests (Sid, hascovid, positivedate)
                VALUES (%s, %s, %s)
                '''

insert_vaccination_records = '''
                INSERT INTO Vaccination (Sid, lastdosedate, numdoses, dosetype)
                VALUES (%s, %s, %s, %s)
                '''

insert_enrolled_records = '''
                INSERT INTO Enrolled (Cid, Sid)
                VALUES (%s,%s)
                '''

insert_participates_records = '''
                INSERT INTO Participates (Orgid, Sid)
                VALUES (%s,%s)
                '''


try:
	with connect(
		host="localhost",
		user=input("Enter username: "),
		password=getpass("Enter password: "),
		database="covid_tracker_DB"
	) as connection:
		with connection.cursor() as cursor:
			#cursor.execute(create_DB_query)
			cursor.execute(create_Student_table_query)
			for i,row in df_stud.iterrows():
            			sql = "INSERT INTO covid_tracker_DB.Student VALUES (%s,%s)"
            			cursor.execute(sql, tuple(row))
            			#cursor.commit()
			cursor.execute(create_Section_table_query)
			for i,row in df_sect.iterrows():
            			sql = "INSERT INTO covid_tracker_DB.Section VALUES (%s,%s)"
            			cursor.execute(sql, tuple(row))
            			#cursor.commit()
			cursor.execute(create_Orgainzations_table_query)
			for i,row in df_org.iterrows():
            			sql = "INSERT INTO covid_tracker_DB.Organizations VALUES (%s,%s,%s)"
            			cursor.execute(sql, tuple(row))
            			#cursor.commit()
			cursor.execute(create_Tests_table_query)
			for i,row in df_tests.iterrows():
            			sql = "INSERT INTO covid_tracker_DB.Tests VALUES (%s,%s)"
            			cursor.execute(sql, tuple(row))
            			#cursor.commit()
			cursor.execute(create_Vaccination_table_query)
			for i,row in df_vax.iterrows():
            			sql = "INSERT INTO covid_tracker_DB.Vaccination VALUES (%s,%s,%s,%s)"
            			cursor.execute(sql, tuple(row))
            			#cursor.commit()
			cursor.execute(create_Enrolled_table_query)
			for i,row in df_enroll.iterrows():
            			sql = "INSERT INTO covid_tracker_DB.Enrolled VALUES (%s,%s)"
            			cursor.execute(sql, tuple(row))
            			#cursor.commit()
			cursor.execute(create_Participates_table_query)
			for i,row in df_part.iterrows():
            			sql = "INSERT INTO covid_tracker_DB.Participates VALUES (%s,%s)"
            			cursor.execute(sql, tuple(row))
            			#cursor.commit()
			connection.commit()
except Error as e:
	print(e)
