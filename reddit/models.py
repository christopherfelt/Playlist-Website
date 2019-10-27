from django.db import models
from accounts import models as acc_models

# Create your models here.
class Subreddit(models.Model):

    submission_option = [('track','track'), ('album','album'),('playlist','playlist')]

    user = models.ForeignKey(to=acc_models.User, on_delete=models.CASCADE)
    subreddit = models.CharField(max_length=100)
    submission_type = models.CharField(max_length=100, choices=submission_option)
    spotify_id = models.CharField(max_length=100)
