from django.db import models


class Task(models.Model):
    STATUS_OPTION = (
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('postponed', 'Postponed')
    )

    CATEGORY_OPTIONS = (
        ('urgent', 'Urgent'),
        ('important', 'Important'),
        ('needs_to_be_done', 'Needs to be done'),  
    )

    description = models.CharField(max_length=400)
    creation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=25, choices=CATEGORY_OPTIONS, default='important')
    status = models.CharField(max_length=25, choices=STATUS_OPTION, default='pending')