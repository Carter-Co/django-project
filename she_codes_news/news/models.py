from django.contrib.auth import get_user_model
from django.db import models

CATEGORY_OPTIONS = [
    ('C', 'Cohort'),
    ('M', 'Mentors'),
    ('P', 'Pilbara'),
]

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=200, choices = CATEGORY_OPTIONS, default='P')
    content = models.TextField()
    image_url = models.URLField(max_length=200)