from django.contrib import admin

from .models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'foundation',
        'country',
        'city',
        'specialisation',
        'partnership',
        'description'
    )
    search_fields = 'name',
    list_display = (
        'name',
        'foundation',
        'country',
        'city',
        'specialisation',
        'id'
    )
    list_filter = (
        'country',
        'city',
        'specialisation'
    )


admin.site.register(Company, CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    fields = (
        'company',
        'position',
        'name',
        'age'
    )
    list_display = (
        'name',
        'company',
        'position',
        'age',
        'id'
    )
    list_filter = (
        'position',
        'age',
        'company'
    )
    search_fields = 'name',


admin.site.register(Employee, EmployeeAdmin)
