from rest_framework import serializers
from trade.models import CommoDityModel

class CommoDitySerializer(serializers.Serializer):

    id = serializers.IntegerField(label='ID',read_only=True)

    commo_type = serializers.CharField(label='種類',max_length=50,required=False)

    seller = serializers.CharField(label='賣家',max_length=50,required=False)

    rarity = serializers.CharField(label='稀有度',max_length=50,required=False)

    ability = serializers.StringRelatedField(label="能力",read_only=True) 

    commo_money = serializers.IntegerField(label='金額',required=False)

    create_time = serializers.CharField(label='創建時間',max_length=50,required=False)

    renew_time = serializers.CharField(label="最後更新時間",max_length=50,required=False)

    is_deleted = serializers.BooleanField(label='是否刪除',required=False)
 
    class Meta:
        model = 'CommoDity'
        fields = ('id', 'create_time','renew_time','is_deleted','commo_type', 'seller', 'rarity', 'commo_money')
        # fields = '__all__'