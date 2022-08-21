from rest_framework import serializers 
from tutorials.models import Tutorial

class OffFieldAppSerializer(serializers.ModelSerializer):

    class Mete:
        model = OffFieldApp
        fields = ('xx',
                'xx',
                'xx',
                'xx')