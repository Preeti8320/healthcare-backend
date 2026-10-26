from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Patient
        fields = '__all__'

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.name')
    doctor_name = serializers.ReadOnlyField(source='doctor.name')

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'assigned_at')