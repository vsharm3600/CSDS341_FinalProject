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

#insertion queries
insert_student_records = '''
                INSERT INTO  Student (Sid, Address)
                VALUES (%s,%s)
                '''

insert_residence_records = '''
                INSERT INTO Residence (Address)
                VALUES (%s)
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
		database="covid_tracker_DB"d
	) as connection:
		with connection.cursor() as cursor:
			#cursor.execute(create_DB_query)
			#cursor.execute(create_Student_table_query)
			#cursor.execute(create_Residence_table_query)
			#cursor.execute(create_Section_table_query)
			#cursor.execute(create_Orgainzations_table_query)
			#cursor.execute(create_Tests_table_query)
			#cursor.execute(create_Vaccination_table_query)
			#cursor.execute(create_Enrolled_table_query)
			#cursor.execute(create_Participates_table_query)
			#connection.commit()
			cursor.executemany(insert_student_records, df_stud.values.tolist())
			cursor.executemany(insert_residence_records, df_resid.values.tolist())
			cursor.executemany(insert_section_records, df_sect.values.tolist())
			cursor.executemany(insert_organization_records, df_org.values.tolist())
			cursor.executemany(insert_tests_records, df_tests.values.tolist())
			cursor.executemany(insert_vaccination_records, df_vax.values.tolist())
			cursor.executemany(insert_enrolled_records, df_enroll.values.tolist())
			cursor.executemany(insert_participates_records, df_part.values.tolist())
			connection.commit()
except Error as e:
	print(e)