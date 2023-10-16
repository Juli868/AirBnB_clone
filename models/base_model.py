#!/usr/bin/python3
"""Class definition."""
import models
import uuid
import datetime


class BaseModel:
    """Define the class attriutes and methods."""

    def __init__(self, *args, **kwargs):
        """Initialize an instance."""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    self.__class__ = globals().get(v, self.__class__)
                    del kwargs[k]
                elif k in ['created_at', 'updated_at']:
                    v = datetime.datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """Transform the object to dicitnary."""
        final = self.__dict__.copy()
        final["created_at"] = self.created_at.isoformat()
        final["updated_at"] = self.updated_at.isoformat()
        final["__class__"] = self.__class__.__name__
        return final

    def __str__(self):
        """Return the str representation of an object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
