from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    
    create_time = models.DateField(default=timezone.now,verbose_name="上傳時間")

    renew_time = models.DateField(default=timezone.now,verbose_name="最後更新時間")
    class Meta:
        abstract = True