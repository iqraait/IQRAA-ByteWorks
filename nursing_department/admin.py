from django.contrib import admin
from .models import Staff, Form1_assement

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'designation', 'employee_id', 'location')
    search_fields = ('staff_name', 'employee_id', 'designation')
    list_filter = ('designation', 'location')

@admin.register(Form1_assement)
class Form1AssementAdmin(admin.ModelAdmin):
    list_display = (
        'staff',
        'evaluation_period',
        'evaluator_name',
        'total_score',
        'percentage',
        'evaluation_date',
    )
    list_filter = ('evaluation_period', 'evaluation_date')
    search_fields = ('staff__staff_name', 'evaluator_name__name')  # Assuming Employee has a 'name' field
    date_hierarchy = 'evaluation_date'
    ordering = ('-evaluation_date',)

    # Optional: Customize form display (e.g., grouping fields)
    fieldsets = (
        ('Basic Information', {
            'fields': ('staff', 'evaluation_period', 'evaluator_name'),
        }),
        ('Scores', {
            'fields': ('total_score', 'percentage', 'data'),
        }),
    )

    # Optional: Make evaluator_name a searchable dropdown (if Employee has many records)
    raw_id_fields = ('evaluator_name',)

