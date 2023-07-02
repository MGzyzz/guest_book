from django.db import models


class Guest_book(models.Model):
    name = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Name'
    )
    email_author = models.EmailField(
        max_length=254,
        null=False,
        blank=False,
        verbose_name='Email'
    )
    entry_text = models.TextField(
        max_length=5000,
        null=False,
        blank=False,
        verbose_name='Entry text'
    )
    time_of_creation = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name='Time of creations'
    )
    edit_time = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
        verbose_name='Edit time'
    )

    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES, default='active',
        null=False,
        blank=False,
        verbose_name='Status'
    )

    def __str__(self):
        return self.name
# Create your models here.
