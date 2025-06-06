from django.db import models
from hospitals.models import Hospital
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

class BloodDonation(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'pending'),
        ('Appointed', 'appointed'),
        ('Completed', 'completed'),
    ]
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('unknown', 'unknown'),
    ]
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,null=False)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()   
    email = models.EmailField()
    age = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPE_CHOICES)
    last_donation_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # Health Screening Questions
    recent_illness = models.BooleanField()
    taking_antibiotics = models.BooleanField()
    heart_disease = models.BooleanField()
    pregnant_or_given_birth = models.BooleanField()
    blood_transfusion_last_year = models.BooleanField()
    traveled_malaria_risk_area = models.BooleanField()
    hepatitis_or_hiv = models.BooleanField()
    tattoo_or_piercing_last_six_months = models.BooleanField()
    meets_eligibility = models.BooleanField()
    id_card = models.ImageField(upload_to='ID_card/', blank=True, null=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.blood_type}"
    
# models.py
class BloodDonationRequest(models.Model):
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O-'), ('O-', 'O-'),
        ('unknown', 'unknown'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'pending'),
        ('Appointed', 'appointed'),
        ('Completed', 'completed'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blood_requests')
    request_date = models.DateTimeField(default=timezone.now)
    patient_name = models.CharField(max_length=100)
    blood_product = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    transfusion_rate = models.CharField(max_length=100)
    reason = models.TextField()
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPE_CHOICES, default='unknown')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.patient_name} - {self.blood_product}"
    