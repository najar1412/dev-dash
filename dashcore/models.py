from django.db import models

# Create your models here.
from django.db import models
from mongoengine import *

# Create your models here.

class Personal(Document):
    # Person
    username = StringField(required=True)
    email = StringField(required=True)
    user_image = StringField(max_length=255)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    start_date = StringField(max_length=50)
    cakeday = StringField(max_length=50)
    role = StringField(max_length=50)
    rate = StringField(max_length=50)

    # Benifit
    holiday = StringField(max_length=50)

    # Health
    med_provider = StringField(max_length=50)
    med_plan = StringField(max_length=50)
    dent_provider = StringField(max_length=50)
    dent_plan = StringField(max_length=50)

    # Project
    curr_project = StringField(max_length=50)
    pre_project = StringField(max_length=50)


    # Comment
    sent_note = StringField(max_length=200)
    recv_note = StringField(max_length=200)
