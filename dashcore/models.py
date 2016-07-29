from django.contrib.postgres.fields import ArrayField
from django.db import models

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
    rank = models.CharField(max_length=50, default=1)

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

    def __str__(self):
        return 'Member Object: {} {}'.format(self.first_name, self.last_name)


class Project(models.Model):
    # Project
    code = models.CharField(max_length=50)
    inc = models.CharField(max_length=50)
    name = models.CharField(max_length=255, default='No Name')
    start = models.CharField(max_length=255, blank=True)
    end = models.CharField(max_length=255, blank=True)
    creator_id = models.CharField(max_length=255, blank=True)
    assigned_user_id = models.CharField(max_length=500, blank=True)

    asset = ArrayField(models.CharField(max_length=100), blank=True, default=list)

    location = models.CharField(max_length=1000, blank=True)
    signedoff = models.BooleanField(default=False, blank=True)
    flagdelete = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return 'Project Object: {}: {}, {}'.format(self.code, self.inc, self.name)

class Asset(models.Model):
    # Asset
    collection = models.CharField(max_length=100, default='False')
    project_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    item_thumb = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    member_id = models.CharField(max_length=1000)

    def __str__(self):
        return 'Asset Object: {}'.format(self.name)
