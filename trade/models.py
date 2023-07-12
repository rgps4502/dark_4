from django.db import models
from base.basemodel import BaseModel
# Create your models here.


class CommoDityModel(BaseModel):
    commo_type = models.CharField(max_length=50, verbose_name="種類")

    seller = models.CharField(max_length=50, verbose_name="賣家")

    rarity = models.CharField(max_length=50, verbose_name="稀有度")

    commo_money = models.IntegerField(verbose_name="商品金額")




    def __str__(self):
        return self.seller


class MessageModel(BaseModel):
    # 需要去關聯留言人
    # user = models.CharField(max_length=255, verbose_name="留言人")
    message = models.CharField(max_length=255, verbose_name="留言板")

    # def __str__(self):
    #     return self.user