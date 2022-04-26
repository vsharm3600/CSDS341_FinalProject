import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error

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
		
try:
	with connect(
		host="localhost",
		user=input("Enter username: "),
		password=getpass("Enter password: "),
		database="covid_tracker_DB"
	) as connection:
		with connection.cursor() as cursor:
			cursor.execute(create_Student_table_query)
			cursor.execute(create_Residence_table_query)
			cursor.execute(create_Section_table_query)
			cursor.execute(create_Orgainzations_table_query)
			cursor.execute(create_Tests_table_query)
			cursor.execute(create_Vaccination_table_query)
			cursor.execute(create_Livesin_table_query)
			cursor.execute(create_Enrolled_table_query)
			cursor.execute(create_Participates_table_query)
			connection.commit()
except Error as e:
	print(e)