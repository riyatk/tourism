from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor', 'status', 'expiry_date','image','price']
    list_filter = ['status']
    actions = ['approve_packages']

    def approve_packages(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f"{updated} packages approved.")
    approve_packages.short_description = "Approve selected packages"
