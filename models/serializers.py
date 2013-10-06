from models import LiftData, LiftHistory, LiftSet
from rest_framework import serializers
        
class LiftDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftData
        fields = ['id', 'name', 'user', 'history', ]

class LiftHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftHistory
        fields = ['id', 'one_rep_max', 'date', 'week', 'cycle', 'sets', ]

class LiftSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftSet
        fields = ['id', 'set', 'reps', 'weight', ]