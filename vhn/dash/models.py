from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        str_name = '{}, {}'.format(self.first_name[:1], self.second_name)
        return '{}:{}'.format(self.id, str_name)

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    start_date = models.DateTimeField('start date', default=0)
