from django.db import models

from .user import User

class Event(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  place = models.CharField(max_length=100)
  # deal with this at the end
  # date = models.DateField()
  # time = models.TimeField()
  description = models.CharField(max_length=250)
  # just an idea
  # image = models.CharField(max_length=350)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return self.name

  def as_dict(self):
    """Returns dictionary version of Event models"""
    return {
        'id': self.id,
        'name': self.name,
        'place': self.place,
        # 'date': self.date,
        # 'time': self.time,
        'description': self.description
    }
