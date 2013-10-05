from models import LiftData
from rest_framework import serializers
        
class LiftDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftData
        fields = ['id', 'name', 'one_rep_max', 'user', ]
