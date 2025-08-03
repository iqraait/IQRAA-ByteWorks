from django.contrib import admin
from .models import NursingModelListing

@admin.register(NursingModelListing)
class NursingModelListingAdmin(admin.ModelAdmin):
    # Display fields in list view
    list_display = ('iqraa_id', 'staff_name', 'nursing_station', 'statues', 'form_pdf','uploaded_at')
    
    # Make fields clickable for editing
    list_display_links = ('iqraa_id', 'staff_name')
    
    # Add filters for these fields
    list_filter = ('nursing_station', 'statues', 'uploaded_at')
    
    # Enable search on these fields
    search_fields = ('iqraa_id', 'staff_name', 'nursing_station')
    
    # Fields to show in edit form (grouped logically)
    fieldsets = (
        ('Staff Information', {
            'fields': ('iqraa_id', 'staff_name', 'nursing_station')
        }),
        ('Form Details', {
            'fields': ('statues', 'form_pdf')
        }),
        ('Metadata', {
            'fields': ('uploaded_at',),
            'classes': ('collapse',)  # Makes this section collapsible
        })
    )
    
    #    
    # Custom list actions
    actions = ['mark_as_completed']

    readonly_fields = ['uploaded_at']
    
    # Items per page
    list_per_page = 25
    
