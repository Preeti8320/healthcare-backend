from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Authenticated user ke banaye gaye patients hi return honge
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)