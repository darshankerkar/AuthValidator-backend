from django.urls import path
from .views import OCRView, BulkCertificateUploadView

urlpatterns = [
    path('', OCRView.as_view(), name='ocr'),
    path('bulk-upload/', BulkCertificateUploadView.as_view(), name='bulk-upload'),
]
