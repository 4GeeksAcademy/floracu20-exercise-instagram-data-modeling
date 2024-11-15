import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(40), nullable=False, unique=True)
    comments = relationship('comment', back_populates="author_relationship")
    followers = relationship('Follower', back_populates="followed_user")
    following = relationship('Follower', back_populates="follower_user")

class Follower(Base):
    __tablename__='follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    follower_user = relationship('User', back_populates = 'following')

    user_to_id = Column(Integer, ForeignKey('user.id'))
    followed_user = relationship('User', back_populates = 'followers')    

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    author_relationship = relationship('User', back_populates="comments")
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates="comments")

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comments = relationship('Comment', back_populates="post")

## Draw from SQLAlchemy base
try: 
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
