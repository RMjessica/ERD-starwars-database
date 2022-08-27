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
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    last_name = Column(String(30))
    username = Column(String(20), unique=True)
    email = Column(String(40), unique=True)
    password = Column(String(20))
    creation_date = Column(
        String(10), default=get_current_date, nullable=False)

    favorite = relationship('Favorite', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email,
            "creation_date": self.creation_date
        }


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    gender = Column(String(20))
    birth_date = Column(String(10))
    height = Column(Integer)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    skin_color = Column(String(50))
    url_image = Column(String(200), unique=True, )
    description = Column(String(200), unique=True)

    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet', back_populates='character')

    favorite = relationship('Favorite', back_populates='character')
    vehicle = relationship('Vehicle', back_populates='character')
    starship = relationship('Starship', back_populates='character')

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "height": self.height,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "url_image": self.url_image,
            "description": self.description,
            "planet_id": self.planet_id
        }


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    population = Column(Integer)
    terrain = Column(String(50))
    climate = Column(String(50))
    orbit_period = Column(Integer)
    orbit_rotation = Column(Integer)
    diameter = Column(Integer)
    url_image = Column(String(200), unique=True)
    description = Column(String(200), unique=True)

    favorite = relationship('Favorite', back_populates='planet')
    character = relationship('Character', back_populates='planet')

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
            "orbit_period": self.orbit_period,
            "orbit_rotation": self.orbit_rotation,
            "diameter": self.diameter,
            "url_image": self.url_image,
            "description": self.description,
        }


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    model = Column(String(100))
    vehicle_class = Column(String(100))
    passengers = Column(Integer)
    max_speed = Column(Integer)
    consumables = Column(Integer)
    url_image = Column(String(200), unique=True)
    description = Column(String(200), unique=True)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character', back_populates='vehicle')

    favorite = relationship('Favorite', back_populates='vehicle')

    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "passengers": self.passengers,
            "max_speed": self.max_speed,
            "consumables": self.consumables,
            "url_image": self.url_image,
            "description": self.description,
            "character_id": self.character_id
        }


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    model = Column(Integer)
    manufacturer = Column(String(120))
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    created = Column(String(70))
    consumables = Column(Integer)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character', back_populates='starship')

    favorite = relationship('Favorite', back_populates='starship')

    def __repr__(self):
        return '<Starship %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "created": self.created,
            "consumables": self.consumables,
            "character_id": self.character_id
        }


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favorite')

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character', back_populates='favorite')

    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet', back_populates='favorite')

    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship('Vehicle', back_populates='favorite')

    starship_id = Column(Integer, ForeignKey('starship.id'))
    starship = relationship('Starship', back_populates='favorite')

    def __repr__(self):
        return 'Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
            "starship_id": self.starship_id,
        }


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
