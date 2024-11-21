from django.db import models

class Currency(models.Model):
  code = models.CharField(max_length=3)
  reverse_rate = models.BooleanField(default=False)