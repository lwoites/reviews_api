from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    verbose_name_plural = 'companies'

    def __str__(self):
        return self.name
    


class Review(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)

    # we don't want to remove the review if the user was deleted
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    reviewer_ip = models.GenericIPAddressField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.title[0:16]