from django.db import models

from django.contrib.postgres.fields import JSONField
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    data = JSONField()


class SKU(TimeStampedModel):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    data = JSONField()
