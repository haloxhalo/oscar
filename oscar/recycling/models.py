from django.contrib.postgres.fields import JSONField
from model_utils.models import TimeStampedModel


class RecyclingCenter(TimeStampedModel):
    data = JSONField()
