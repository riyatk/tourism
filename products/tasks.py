from celery import shared_task
from django.utils import timezone
from .models import Package

@shared_task
def expire_old_packages():
    today = timezone.now().date()
    expired = Package.objects.filter(expiry_date__lt=today, status='approved')
    count = expired.update(status='expired')
    return f"{count} packages expired"
