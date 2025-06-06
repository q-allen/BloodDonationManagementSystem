from rest_framework import generics
from .models import BloodDonation, BloodDonationRequest
from rest_framework import generics, status
from .serializers import BloodDonationSerializer, BloodDonationRequestSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
import logging

class AppointedRecordsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        donations = BloodDonation.objects.filter(status__iexact="Appointed")
        requests = BloodDonationRequest.objects.filter(status__iexact="Appointed")

        donation_data = BloodDonationSerializer(donations, many=True).data
        request_data = BloodDonationRequestSerializer(requests, many=True).data

        return Response({
            "appointed_donations": donation_data,
            "appointed_requests": request_data
        })



class BloodDonationCreateView(generics.CreateAPIView):
    queryset = BloodDonation.objects.all()
    serializer_class = BloodDonationSerializer

class BloodDonationRequestCreateView(generics.CreateAPIView):
    serializer_class = BloodDonationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

  