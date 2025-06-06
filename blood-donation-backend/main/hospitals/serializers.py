from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)  # Returns full URL

    class Meta:
        model = Hospital
        fields = ['id', 'name', 'description', 'location', 'image', 'contact_number']