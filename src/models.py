import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    password = Column(String(12), nullable=False)
    creation_date = Column(
        String(10), default=get_current_date, nullable=False)

    favorite = relationship('Favorite', back_populates='user')


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    gender = Column(String(20), nullable=False)
    birth_date = Column(String(10), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    url_image = Column(String(200), unique=True, nullable = False, )
    description = Column(String(1000), unique=True, nullable = False)

    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet', back_populates='character')

    favorite = relationship('Favorite', back_populates='user')
    vehicles = relationship('Vehicle', back_populates='character')
    starship = relationship('Starship', back_populates='starship')

    
class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    population = Column(Integer, nullable = False)
    terrain = Column(String(50), nullable = False)
    climate = Column(String(50), nullable = False)
    orbit_period = Column(Integer, nullable = False)
    orbit_rotation = Column(Integer, nullable = False)
    diameter = Column(Integer, nullable = False)
    url_image = Column(String(200), unique = True, nullable = False)
    description = Column(String(1000), unique = True, nullable = False)

    favorite = relationship('Favorite', back_populates='planet')
    character = relationship('Character', back_populates='planet')

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    model = Column(String(100), nullable = False)
    vehicle_class = Column(String(100), unique = True, nullable = False)
    passengers = Column(Integer, nullable = False)
    max_speed = Column(Integer, nullable = False)
    consumables = Column(Integer, nullable = False)
    url_image = Column(String(200), unique = True, nullable = False)
    description = Column(String(1000), unique = True, nullable = False)

    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character', back_populates='vechicle')

    favorite = relationship('Favorite', back_populates='vehicle')


class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character', back_populates='starship')

    favorite = relationship('Favorite', back_populates='starship')


class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='favorite')

    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character', back_populates='favorite')

    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet', back_populates='favorite')

    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship('Vehicle', back_populates='favorite')

    starship_id = Column(Integer, ForeignKey('starships.id'))    
    starship = relationship('Starship', back_populates='favorite')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')