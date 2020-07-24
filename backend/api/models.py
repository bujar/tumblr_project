from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class TumblrCache(models.Model):
    tumblr_name = models.CharField(max_length=70, blank=False, primary_key=True)
    json_response = JSONField()
