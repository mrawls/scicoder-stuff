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
# we'll save it as arrays of strings (one per column)
first_names, last_names, cities, supervisors, statuses, clubs = np.loadtxt(data, comments='#',
	dtype=(np.str_), skiprows=5, delimiter='|', usecols=(0,1,2,3,4,5), unpack=True)

### loop through each entry in the arrays created above ###
for i in range(0,len(last_names)):
	
	# create a student object
	s = Student()
	s.first_name = first_names[i]
	s.last_name = last_names[i]
	session.add(s)
	
	# next, create a city object
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
	
	# repeat this process for clubs
	# students can be in more than one club, or none
	clublist = clubs[i].split(', ')
	for j in range(0,len(clublist)):
		if clublist[j] != '': # maybe the student isn't in any clubs
			# see if the club is already in the database
			try:
				one_club = session.query(Club).filter(Club.label==clublist[j]).one()
			# if it isn't, then add it
			except sqlalchemy.orm.exc.NoResultFound:
				one_club = Club()
				one_club.label = clublist[j]
				session.add(one_club)
			# connect the club info to the student
			# since a student can have more than one club, we append it
			s.clubs.append(one_club)
	
	# repeat this process for status
	# see if the status is already in the database
	try:
		one_status = session.query(Status).filter(Status.label==statuses[i]).one()
	# if it isn't, then add it
	except sqlalchemy.orm.exc.NoResultFound:
		one_status = Status()
		one_status.label = statuses[i]
		session.add(one_status)
	# connect the city info to the student
	s.status = one_status
	
	# repeat this process for supervisor
	# students can have more than one supervisor, or none
	supervisorlist = supervisors[i].split(', ')
	for j in range(0,len(supervisorlist)):
		if supervisorlist[j] != '': # maybe the student doesn't have a supervisor
			# see if the supervisor is already in the database
			try:
				one_supervisor = session.query(Supervisor).filter(Supervisor.last_name==supervisorlist[j].split('/')[0]).one()
			# if they aren't, then add them
			except sqlalchemy.orm.exc.NoResultFound:
				one_supervisor = Supervisor()
				one_supervisor.last_name = supervisorlist[j].split('/')[0]
				one_supervisor.room_number = supervisorlist[j].split('/')[1]
				session.add(one_supervisor)
			# connect the supervisor info to the student
			# since a student can have more than one supervisor, we append them
			s.supervisors.append(one_supervisor)

### now we're done adding info to the database; save & exit nicely ###
session.commit()
engine.dispose() # cleanly disconnect from the database
sys.exit(0)
