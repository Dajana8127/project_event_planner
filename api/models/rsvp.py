from django.db import models

from .user import User
from .event1 import Event

class RSVP(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )
  event = models.ForeignKey(
      Event,
      related_name='rsvps',
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return self.event

  def as_dict(self):
    """Returns dictionary version of Event models"""
    return {
        'id': self.id,
        'event': self.event,
        'owner': self.owner
    }
