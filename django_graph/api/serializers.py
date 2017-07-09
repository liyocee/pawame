from rest_framework import serializers
from .models import RandomNumber

class RandomNumberSerializer(serializers.ModelSerializer):
    created_on = serializers.SerializerMethodField()

    class Meta:
        model = RandomNumber
        fields = ('number', 'created_on')

    def get_created_on(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
