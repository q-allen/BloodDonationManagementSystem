from django.contrib import admin
from .models import BloodDonation, BloodDonationRequest
# Register your models here.
admin.site.register(BloodDonation)
admin.site.register(BloodDonationRequest)