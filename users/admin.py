from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Employee, Department

class EmployeeChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee

class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ('iqraa_id', 'department')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)
    search_fields = ('department_name',)

class EmployeeAdmin(UserAdmin):
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm
    
    # Admin list view
    list_display = ('iqraa_id', 'department', 'is_active', 'is_staff', 'is_superuser', 'created')
    list_filter = ('iqraa_id','department', 'is_staff', 'is_superuser')
    list_editable = ('is_active', 'is_staff')
    
    # Fields organization in edit view
    fieldsets = (
        (None, {'fields': ('iqraa_id', 'password')}),
        ('Personal Info', {'fields': ('department',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 
                      'groups', 'user_permissions'),
        }),
        ('Important Dates', {'fields': ('last_login', 'created', 'updated')}),
    )
    
    # Fields for add/create view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('iqraa_id', 'department', 'password1', 'password2'),
        }),
    )
    
    # Search and ordering
    search_fields = ('iqraa_id',)
    ordering = ('-created',)
    filter_horizontal = ('groups', 'user_permissions',)
    
    # Timestamp and soft-delete handling
    readonly_fields = ('created', 'updated', 'last_login')
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(soft_delete=False)

# Register models
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)