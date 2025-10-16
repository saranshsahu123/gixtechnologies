from django.contrib import admin
from .models import Applicant

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'feedback')
    search_fields = ('name', 'email', 'mobile')
