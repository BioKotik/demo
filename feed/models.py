from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Record(models.Model):
    STATE = (
        ('draft', 'Draft'),
        ('published', "Published"),
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    state = models.CharField(max_length=10,
                             choices=STATE,
                             default='draft')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='all_records')
    pub = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title