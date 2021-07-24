#!/usr/bin/python3
""" Module: User
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Class that defines a user by attributes"""
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
