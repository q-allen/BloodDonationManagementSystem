from django.urls import path
from .views import AppointedRecordsView, BloodDonationCreateView, BloodDonationRequestCreateView

urlpatterns = [
    path('blood_donation/', BloodDonationCreateView.as_view(), name='blood-donation-create'),
    path('request-blood/', BloodDonationRequestCreateView.as_view(), name='request-blood'),
    path('appointed-records/', AppointedRecordsView.as_view(), name='appointed-records'),
]
