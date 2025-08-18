from django.contrib import admin
from .models import Patient_Registration, Address, Department, Doctor

class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

@admin.register(Patient_Registration)
class PatientAdmin(admin.ModelAdmin):
    inlines = [AddressInline]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor_count')
    
    def doctor_count(self, obj):
        return obj.doctors.count()

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)
    search_fields = ('name',)