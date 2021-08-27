# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 02:33:31 2021

@author: Julian Brink
"""

import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

import pandas as pd
#import pyodbc # not included in anaconda: pip install pyodbc
#import os

"""
engine = sqla.create_engine(
    "mssql+pyodbc://pyconnect:123456@DESKTOP-M98MIFO\SQLEXPRESS/DiscGolf"
    "?driver=ODBC+Driver+17+for+SQL+Server")
"""
engine = sqla.create_engine('sqlite+pysqlite:///../data/discy.db', echo=True)

metadata = sqla.MetaData()
Base = declarative_base()
session = Session(engine, future=True)

"""
courses = sqla.Table("courses", metadata, autoload_with=engine)
layouts = sqla.Table("layouts", metadata, autoload_with=engine)
layout_versions = sqla.Table("layout_versions", metadata, autoload_with=engine)

stmt = sqla.select(courses).where(courses.c.course_name == 'alpha')
select_all = sqla.select(courses)
result = session.execute(select_all).all()
"""

def get_table_courses():
    df_courses = pd.read_sql_table(
    "courses",
    con=engine,
#    schema='public',
#    index_col='course_id',
    coerce_float=False,
    columns=['course_name'])
    return df_courses

def get_table_layouts():
    df_layouts = pd.read_sql_table(
    "layouts",
    con=engine,
#    schema='public',
#    index_col='layout_id',
    coerce_float=False,
    columns=[
        'course_name',
        'layout_name'])
    return df_layouts

    
def get_table_layout_versions():
    df_layout_versions = pd.read_sql_table(
    "layout_versions",
    con=engine,
#    schema='public',
#    index_col='version_id',
    coerce_float=False,
    columns=[
        'version',
        'course_name',
        'layout_name',
        'oldest',
        'newest',
        'holes',
        'par',
    ],
#    chunksize=500
)
    return df_layout_versions


def get_table_scoredata():
    df_scoredata = pd.read_sql_table(
    "scoredata",
    con=engine,
#    schema='public',
#    index_col='version_id',
    coerce_float=False,
    columns=[
        'version_id',
        'course_name',
        'layout_name',
        'teamsize',
        'Date',
        'holes',
        'par',
    ],
#    chunksize=500
)
    return df_scoredata
