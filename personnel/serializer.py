from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department,Personnel

class FixModel(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField(required=False)


class DepartmentSerializer(FixModel):
    # user=serializers.StringRelatedField()
    # user_id=serializers.IntegerField(required=False)

    #metodFieldlar sadece readonly dir.
    personnel_count=serializers.SerializerMethodField()  #her personelde bir sayi ekle
    class Meta:
        model=Department
        fields="__all__"

    def get_personel_count(self, obj):
       return obj.personnels.count()

class PersonnelSerializer(FixModel):
    # user=serializers.StringRelatedField()
    # user_id=serializers.IntegerField(required=False)
    class Meta:
        model=Personnel
        fields="__all__"
   
    
    