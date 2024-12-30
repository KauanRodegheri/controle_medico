from rest_framework import serializers
from .models import Drug

class DrugModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drug
        fields = ['id', 'user', 'name']