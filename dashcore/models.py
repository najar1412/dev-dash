from django.db import models
# from mongoengine import *

# Create your models here.

class Member(models.Model):
    # member
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_image = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    cakeday = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)

    # Benifit
    holiday = models.CharField(max_length=50)

    # Health
    med_provider = models.CharField(max_length=50)
    med_plan = models.CharField(max_length=50)
    dent_provider = models.CharField(max_length=50)
    dent_plan = models.CharField(max_length=50)

    # Project
    curr_project = models.CharField(max_length=50)
    pre_project = models.CharField(max_length=50)

    # asset
    assign_asset = models.CharField(max_length=1000)

    # Comment
    sent_note = models.CharField(max_length=200)
    recv_note = models.CharField(max_length=200)

class Project(models.Model):
    # Project
    code = models.CharField(max_length=50)
    inc = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)

    creator_id = models.CharField(max_length=255, default='0')
    assigned_user_id = models.CharField(max_length=500)
    asset = models.CharField(max_length=500)

    location = models.CharField(max_length=1000, default='')
    signedoff = models.BooleanField(default=False)
    flagdelete = models.BooleanField(default=False)

class Asset(models.Model):
    # Asset
    collection = models.CharField(max_length=100, default='False')
    project_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    item_thumb = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    member_id = models.CharField(max_length=1000)
