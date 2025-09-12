from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(ImportExportModelAdmin):
    pass
