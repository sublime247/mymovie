from rest_framework import serializers
from watchlist.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    description= serializers.CharField()
    isActive =serializers.BooleanField()
    
    
    def create(self, validate_data):
       return Movie.objects.create(**validate_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.isActive = validated_data.get('isActive', instance.isActive)
        instance.save()
        
        return instance
    