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

	def __repr__(self):
		return ("If you want to learn about {},you should look at the wikipedia article called {}\n"
			"we gave this article a rating of {} our of 10\n").format(
						self.topic,
						self.article,
						self.rating)

	