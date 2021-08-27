# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:52:02 2021

@author: Julian Brink
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite+pysqlite:///../data/discy.db', echo=True)
Base = declarative_base()


class courses(Base):

    __tablename__ = "courses"
    course_name = Column(String, primary_key=True)
    
    ##relationship hierarchy down
    layouts = relationship("layouts",
                           back_populates="courses")


class layouts(Base):
    __tablename__ = "layouts"
    
    layout_name = Column(String,
                         primary_key=True)
    
    course_name = Column(String,
                         ForeignKey("courses.course_name"),
                         primary_key=True)
    
    ##relationship hierarhcy up
    courses = relationship("courses",
                           back_populates="layouts")
    
    ##relationship hierarchy down
    layout_versions = relationship("layout_versions",
                                   back_populates="layouts")

class layout_versions(Base):
    __tablename__ = "layout_versions"
    
    version = Column(Integer,
                     primary_key=True,
                     nullable=False)
    
    layout_name = Column(String,
                         ForeignKey("layouts.layout_name"),
                         primary_key=True,
                         nullable=False)
    
    course_name = Column(String,
                         ForeignKey("layouts.course_name"),
                         primary_key=True,
                         nullable=False)
    
    oldest = Column(String,
                    nullable=False)
    newest = Column(String,
                    nullable=False)
    holes = Column(Integer,
                   nullable=False)
    par = Column(Integer,
                  nullable=False)
    h1 = Column(Integer)
    h2 = Column(Integer)
    h3 = Column(Integer)
    h4 = Column(Integer)
    h5 = Column(Integer)
    h6 = Column(Integer)
    h7 = Column(Integer)
    h8 = Column(Integer)
    h9 = Column(Integer)
    h10 = Column(Integer)
    h11 = Column(Integer)
    h12 = Column(Integer)
    h13 = Column(Integer)
    h14 = Column(Integer)
    h15 = Column(Integer)
    h16 = Column(Integer)
    h17 = Column(Integer)
    h18 = Column(Integer)
    h19 = Column(Integer)
    h20 = Column(Integer)
    h21 = Column(Integer)
    h22 = Column(Integer)
    h23 = Column(Integer)
    h24 = Column(Integer)
    h25 = Column(Integer)
    h26 = Column(Integer)
    h27 = Column(Integer)

    ##relationship hierarchy up
    layouts = relationship("layouts",
                           back_populates="layout_versions")

    ##relationship hierarchy down
    scores = relationship("scoredata",
                          back_populates="layout_versions")

class scoredata(Base):
    __tablename__ = "scoredata"
    course_name = Column(String,
                         ForeignKey("layout_versions.course_name"),
                         primary_key=True)
    layout_name = Column(String,
                         ForeignKey("layout_versions.layout_name"),
                         primary_key=True)
    layout_version = Column(Integer,
                            ForeignKey("layout_versions.version"),
                            primary_key=True)
    player_name = Column(String,
                 primary_key=True,
                 nullable=False)
    teamsize = Column(Integer,
                 primary_key=True,
                 nullable=False)
    date = Column(String,
                 primary_key=True,
                 nullable=False)
    result = Column(Integer)
    h1 = Column(Integer)
    h2 = Column(Integer)
    h3 = Column(Integer)
    h4 = Column(Integer)
    h5 = Column(Integer)
    h6 = Column(Integer)
    h7 = Column(Integer)
    h8 = Column(Integer)
    h9 = Column(Integer)
    h10 = Column(Integer)
    h11 = Column(Integer)
    h12 = Column(Integer)
    h13 = Column(Integer)
    h14 = Column(Integer)
    h15 = Column(Integer)
    h16 = Column(Integer)
    h17 = Column(Integer)
    h18 = Column(Integer)
    h19 = Column(Integer)
    h20 = Column(Integer)
    h21 = Column(Integer)
    h22 = Column(Integer)
    h23 = Column(Integer)
    h24 = Column(Integer)
    h25 = Column(Integer)
    h26 = Column(Integer)
    h27 = Column(Integer)
    ## relationship hierarchy up
    layout_versions = relationship("layout_versions",
                                   back_populates="scores")


Base.metadata.create_all(engine)

