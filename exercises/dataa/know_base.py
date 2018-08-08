from know import Base, student_data

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(student_name , student_year , student_finished_lab):
	article = student_data(
		student_name = student_name,
		student_year = int(student_year),
		student_finished_lab = boolian(student_finished_lab))
	print(repr(article))
	session.add(article)
	session.commit()


def query_all_articles():
	articles = session.query(student_data).all()
	return articles



def query_article_by_topic(topic):
	articles = session.query(student_data).filter_by(topic = topic).first()
	
	return articles




def delete_article_by_topic(topic):
	articles = session.query(student_data).filter_by(topic = topic).delete()
	session.commit()
	return articles


def delete_all_articles():
	articles = session.query(student_data).delete()
	session.commit()
	return articles

	

def edit_article_rating(updated_rating, article_name):
	new_ar_rate = session.query(student_data).filter_by(article_name = article_name).first()
	new_ar_rate.rating = updated_rating
	session.commit()
	return new_ar_rate

def delete_article_by_rating(threshold):
	articles = session.query(student_data).filter(student_data.rating <= threshold).delete()
	session.commit()
	return articles


	
# name_of = input("what is the name of the article?")
# topic_of = input(" what is the topic of the article?")
# rating_of = int(input("what is the rating that you give to the artice"))
# add_article(name_of,topic_of,rating_of)


# print(query_article_by_topic("ff"))
# delete_all_articles()
# delete_article_by_topic("jj")
# print(query_all_articles())
# print(edit_article_rating(5456456,"car"))
# delete_article_by_rating(23456789098)
