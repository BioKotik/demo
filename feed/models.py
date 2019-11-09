from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

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
    slug = models.SlugField(max_length=250,
                            unique_for_date='pub')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='all_records')
    pub = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('feed:detailed_view',
                       args=[self.pub.year,
                             self.pub.month,
                             self.pub.day,
                             self.slug])

    def __str__(self):
        return self.title