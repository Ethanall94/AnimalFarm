from rest_framework import serializers
from .models import boardPost

class boardPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = boardPost
        fields = '__all__'
