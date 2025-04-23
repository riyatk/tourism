from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Package(models.Model):
    VENDOR = 'vendor'
    ADMIN = 'admin'

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('expired', 'Expired'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    expiry_date = models.DateField()
    image = models.CharField(max_length=45200,blank=True, null=True)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


    def is_expired(self):
        return self.expiry_date < timezone.now().date()




class Profile(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('vendor', 'Vendor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

