from rest_framework import serializers
from .models import Service, Project, ContactMessage



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
    
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Le titre ne peut pas être vide.")
        return value

# class ProjectSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Project
#         fields = '__all__'
    
#     def get_image_url(self, obj):
#         if obj.image:
#             return obj.image.url
#         return None
        
#     def validate_title(self, value):
#         if not value:
#             raise serializers.ValidationError("Le titre ne peut pas être vide.")
#         return value
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Le titre ne peut pas être vide.")
        return value
        

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'