from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class student_data(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = 'students'
	ID = Column(Integer, primary_key=True)
	student_name = Column(String)
	student_year = Column(integer)
	student_finished_lab = Column(Boolean)

	def __repr__(self):
		return ("student name: {}\n"
				"student year: {}\n"
				"student finished lab: {}\n"
	 			"ID: {}").format(
					self.student_namet,
					self.student_year,
					self.student_finished_lab,
					self.ID)

