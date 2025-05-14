from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(min_value=0)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'medical_history', 'created_at']

    def validate_name(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Name should only contain alphabets and spaces.")
        return value

class DoctorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    specialty = serializers.CharField(max_length=100)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact_info', 'created_at']

    def validate_name(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Doctor name should only contain alphabets and spaces.")
        return value

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    # Nested representations for patient and doctor
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    # Accepting IDs for patient and doctor in the request
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source='patient', write_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source='doctor', write_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_at', 'patient_id', 'doctor_id']

    def validate(self, data):
        if data['patient'] == data['doctor']:
            raise serializers.ValidationError("Patient and doctor cannot be the same person.")
        return data
