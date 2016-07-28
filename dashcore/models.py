from django.db import models
from mongoengine import *

# Create your models here.


class Member(Document):
    # member
    username = StringField(required=True)
    email = StringField(required=True)
    user_image = StringField(max_length=255)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    start_date = StringField(max_length=50)
    cakeday = StringField(max_length=50)
    role = StringField(max_length=50)
    rank = StringField(max_length=50)

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

    # asset
    assign_asset = StringField(max_length=1000)

    # Comment
    sent_note = StringField(max_length=200)
    recv_note = StringField(max_length=200)

class Project(Document):
    # Project
    code = StringField(required=True, max_length=50)
    inc = StringField(required=True, max_length=50)
    name = StringField(required=True, max_length=255)
    start = StringField(required=True, max_length=255)
    end = StringField(required=True, max_length=255)

    creator_id = StringField(max_length=255, default='0')
    assigned_user_id = StringField(max_length=500)
    asset = StringField(max_length=500)

    location = StringField(max_length=1000, default='')
    signedoff = BooleanField(default=False)
    flagdelete = BooleanField(default=False)

class Asset(Document):
    # Asset
    collection = StringField(required=False, max_length=100, default='False')
    project_id = StringField(required=False, max_length=100)
    name = StringField(required=False, max_length=100)
    item = StringField(required=False, max_length=100)
    item_thumb = StringField(required=False, max_length=100)
    tag = StringField(required=False, max_length=100)
    member_id = StringField(required=False, max_length=1000)
