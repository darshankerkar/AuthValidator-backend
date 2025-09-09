from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from PIL import Image
import imagehash
from .models import Certificate

class OCRView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response(
                {"status": "failed", "message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST
            )

        file_obj = request.FILES['file']

        try:
            uploaded_img = Image.open(file_obj)
            uploaded_hash = imagehash.average_hash(uploaded_img)

            for cert in Certificate.objects.all():
                stored_img = Image.open(cert.certificate_file.path)
                stored_hash = imagehash.average_hash(stored_img)
                if uploaded_hash - stored_hash < 5:
                    return Response({
                        "status": "success",
                        "message": f"Certificate verified ✅ for {cert.name}"
                    }, status=status.HTTP_200_OK)

            return Response({
                "status": "failed",
                "message": "Certificate not found ❌"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(
                {"status": "failed", "message": f"Failed to process image: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
