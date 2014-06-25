# This program takes information from student_data.txt and puts it into
# a database called my_database.sqlite.
#
# IMPORTANT: this relies on SQLiteConnection.py, DatabaseConnection.py, & ModelClasses.py.
# Make sure you have all the column names defined as classes in ModelClasses.py.

from __future__ import print_function
import sys
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *
import numpy as np

filename = 'student_data.txt'
data = open(filename)

### magical 'connect to database' command ###
# be sure to specify the filename of the .sqlite database in SQLiteConnection.py !!
session = Session()

### read in info from the text file specified above ###
first_names, last_names, cities, supervisors, statuses, clubs = np.loadtxt(data, comments='#',
	dtype=(np.str_), skiprows=5, delimiter='|', usecols=(0,1,2,3,4,5), unpack=True)

#print(first_name)	

### add some primary info to the database ###
for i in range(0,len(last_names)):
	s = Student()
	s.first_name = first_names[i]
	s.last_name = last_names[i]
	session.add(s)
	# see if the city is already in the database
	try:
		one_city = session.query(City).filter(City.label==cities[i]).one()
	# if it isn't, then add it
	except sqlalchemy.orm.exc.NoResultFound:
		one_city = City()
		one_city.label = cities[i]
		session.add(one_city)

	# connect the city info to the student
	s.city = one_city

	### add some supplementary info to the database ###
	#lacrosse = Club()
	#lacrosse.label = "lacrosse"
	#session.add(lacrosse)

	### connect the supplementary info to the students ###
	#s.clubs.append(lacrosse)

### now we're done adding info to the database, and we're going to exit nicely ###
session.commit()
engine.dispose() # cleanly disconnect from the database
sys.exit(0)
