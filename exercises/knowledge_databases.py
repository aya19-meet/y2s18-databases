from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article, topic, rating):
	article_object = Knowledge(
        article = article,
        topic = topic,
        rating = rating)
	session.add(article_object)
	session.commit()


def query_all_articles():
	article = session.query(Knowledge).all()
	return article

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
	topic=topic).all()
	return article
def query_article_by_rating(threshold):
	article = session.query(Knowledge).filter(
	Knowledge.rating<threshold).all()
	return article

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
	topic=topic).delete()
	session.commit()

def delete_all_articles():
	article = session.query(Knowledge).delete()
	session.commit()
 	
def edit_article_rating(new_rating,article):
	article = session.query(
	Knowledge).filter_by(
	article = article).first()
	article.rating = new_rating
	session.commit()
def delete_article_by_rating(threshold):
	article = session.query(Knowledge).filter(
	Knowledge.rating<threshold).delete()
	session.commit()

#delete_all_articles()
#add_article("aliens", "space", 8)
#add_article("the treaty of versailles", "world war", 4)
#add_article("Latin", "dead languages", 3)
print(query_all_articles())
delete_article_by_rating(5)
print(query_all_articles())