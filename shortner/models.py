from faulthandler import disable
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Short_url(models.Model):
    url = models.CharField(max_length=220)
    slug = models.CharField(max_length=20)
    created = models.DateTimeField(default=datetime.now())
    expiration_date = models.DateTimeField(default=datetime.now())
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.url

    

    @property
    def status(self):
        result = self.expiration_date > timezone.now()
        if result:
            return 'Active'
        return 'Expired'
    

             
        