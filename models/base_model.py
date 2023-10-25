#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


class BaseModel:
    """A base class for all hbnb models"""
     id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        data = dict(self.__dict__)
        if "_sa_instance_state" in data:
            del data["_sa_instance_state"]
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
