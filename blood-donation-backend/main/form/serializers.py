from rest_framework import serializers

from hospitals.serializers import HospitalSerializer
from .models import BloodDonation, BloodDonationRequest
from hospitals.models import Hospital

class BloodDonationSerializer(serializers.ModelSerializer):
    hospital_id = serializers.PrimaryKeyRelatedField(
        queryset=Hospital.objects.all(), source='hospital', write_only=True
    )
    hospital = HospitalSerializer(read_only=True)  # Still return hospital details on read

    class Meta:
        model = BloodDonation
        fields = '__all__'
        read_only_fields = ['status']

class BloodDonationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonationRequest
        fields = '__all__'
        read_only_fields = ['user', 'request_date', 'status']