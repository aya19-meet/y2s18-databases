from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'Knowledge'
	some_id = Column(Integer, primary_key=True)
	article = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	def __repr__(self):
			return ("If you want to learn about {},you should look at the wikipedia article called {}\n"
					"we gave this article a rating of {} our of 10\n"
					"ID: {}").format(
						self.topic,
						self.article,
						self.rating
						self.some_id)

	if self.rating>7:
		print("sorry this article is bad")
		