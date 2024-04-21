from rest_framework import serializers
from watchlist.models import Movie



# def name_validator(value):
#       if len(value)<2:
#            raise serializers.ValidationError('Name is too short') 





class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields= "__all__"



    def validate(self, data):
         if data['name']==data['description']:
             raise serializers.ValidationError('Title and description can\'t be thesame')
         else:
             return data
    
    
    def validate_name(self, value):
        if len(value)<2:
            raise serializers.ValidationError('Name is too short') 
        else:
            return value
        
        
        
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name= serializers.CharField(validate= [name_validator])
#     description= serializers.CharField()
#     isActive =serializers.BooleanField()
    
    
#     def create(self, validate_data):
#        return Movie.objects.create(**validate_data)
    
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.isActive = validated_data.get('isActive', instance.isActive)
#         instance.save()
        
#         return instance

        