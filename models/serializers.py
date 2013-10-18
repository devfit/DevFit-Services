from models import LiftData, LiftHistory, LiftSet
from rest_framework import serializers
        
class LiftDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftData
        fields = ['name', 'user', ]

class LiftHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftHistory
        fields = ['id', 'lift_data', 'one_rep_max', 'date', 'week', 'cycle', ]

class LiftSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftSet
        fields = ['id', 'lift_data', 'lift_history', 'set', 'reps', 'weight', ]