from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

#Work on creating relations 

Base = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get('CONNECTION_STRING'))

def create_table(engine):
    Base.metadata.create_all(engine)


class Drink(Base):
    __tablename__='drink'

    id = Column(Integer, primary_key=True)
    name = Column('name', Text())
    price = Column('price', Text()) #Need to change this to int
    link = Column('link', Text())
    type = Column('type', Text())
    origin_place = Column('place', Text())
    percentage = Column('percentage', Text()) #Change to Int
    volume = Column('volume', Text())#Change to Int
    summary = Column('summary', Text())
