from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    
    create_time = models.CharField(max_length=50,default=timezone.now().strftime('%Y-%m-%d %H:%M:%S'),verbose_name="上傳時間")

    renew_time = models.CharField(max_length=50,default=timezone.now().strftime('%Y-%m-%d %H:%M:%S'),verbose_name="最後更新時間")

    is_deleted = models.BooleanField(default=False,verbose_name='是否刪除')
    class Meta:
        abstract = True