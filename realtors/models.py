from django.db import models
from datetime import datetime
# Create your models here.

Class Realtor(models.Model)
    name = models.CharField(max_lenght=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_lenght=20)
    email = models.CharField(max_lenght=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def_str_(self):
        return self.name