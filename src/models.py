import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """


class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(40), nullable=False, unique=True)
    comments = relationship('Comment', back_populates="author_relationship")
    user_from_ids = relationship('Follower', back_populates="user_from_id_relationship")
    user_to_ids = relationship('Follower', back_populates="user_to_id_relationship")

class Follower(Base):
    __tablename__='follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_from_id_relationship = relationship('User', back_populates="user_from_ids")

    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to_id_relationship = relationship('User', back_populates="user_to_ids")    

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    author_relationship = relationship('User', back_populates="comments")
    post_id = Column(Integer, ForeignKey('post.id'))
    post_id_relationship = relationship('Post', back_populates="id_posts")

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    id_posts = relationship('Comment', back_populates="post_id_relationship")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
