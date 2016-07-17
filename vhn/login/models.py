from django.db import models
from mongoengine import *

# Create your models here.

class Personal(Document):
    # Person
    user_image = StringField(max_length=255)
    username = StringField(required=True)
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    role = StringField(max_length=50)

    # TODO: dob and cakeday need to be one entity? But it wont let me only use
    # TODO: one of them :/
    dob = StringField(max_length=50)
    cakeday = StringField(max_length=50)

    start_date = StringField(max_length=50)

    # Benifit
    hols = StringField(max_length=50)

    # Health
    med_provider = StringField(max_length=50)
    med_plan = StringField(max_length=50)
    dent_provider = StringField(max_length=50)
    dent_plan = StringField(max_length=50)

    # Project
    curr_project = StringField(max_length=50)
    pre_project = StringField(max_length=50)

    # Comment

class Project(Document):
    project_code = StringField(required=True, max_length=50)
    project_inc = StringField(required=True, max_length=50)
    project_name = StringField(required=True, max_length=255)
    project_start = StringField(required=True, max_length=255)
    project_end = StringField(required=True, max_length=255)

    creator_id = StringField(max_length=255, default='0')
    assigned_user_id = StringField(max_length=500)

    location = StringField(max_length=1000, default='')
    signedoff = BooleanField(default=False)
    flagdelete = BooleanField(default=False)

class Media(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Comment(Document):
    # make post
    op_id = StringField(required=True)
    item_id = StringField(required=True)
    subject = StringField(required=True)
    content = StringField(default='N/a')
    rate = StringField(default='N/a')

    #reply to post
    parent_id = StringField()
