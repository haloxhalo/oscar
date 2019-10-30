from django.contrib.postgres.fields import JSONField
from model_utils.models import TimeStampedModel


class Scan(TimeStampedModel):
    # data contains:
    #   code: String
    #   lat: Float
    #   lng: Float
    data = JSONField()
