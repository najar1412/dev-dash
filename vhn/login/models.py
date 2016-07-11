from django.db import models
from mongoengine import *

# Create your models here.

class Personal(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Project(Document):
    project_code = StringField(required=True, max_length=50)
    project_inc = StringField(required=True, max_length=50)
    project_name = StringField(required=True, max_length=255)
    project_start = StringField(required=True, max_length=255)
    project_end = StringField(required=True, max_length=255)

    user_id = StringField(max_length=255)

    location = StringField(max_length=1000)
    signedoff = BooleanField(default=False)
    flagdelete = BooleanField(default=False)

class Media(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Comment(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
