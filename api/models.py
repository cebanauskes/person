import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    vector = models.TextField()
    have_vector = models.BooleanField(default=False)