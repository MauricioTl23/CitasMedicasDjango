from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identity_card = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=150,unique=True)
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=20,unique=True)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
    
class Patient(models.Model):
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="patients")
    sure = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    address = models.TextField(null=True)
    
    def __str__(self):
        return f"Paciente: {self.id_user.username} - Seguro: {self.sure}"
    
class Specificity(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="doctors")
    id_specificity = models.ForeignKey(Specificity, on_delete=models.CASCADE, related_name="doctors")
    license_number = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    status = models.BooleanField()
    
    def __str__(self):
        return f"Dr. {self.id_user.first_name} {self.id_user.last_name} - {self.id_specificity.name}"
    
class Office(models.Model):
    name = models.CharField(max_length=50)
    location = models.TextField()
    status = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class Available_Times(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Lunes'),
        ('TUE', 'Martes'),
        ('WED', 'Miercoles'),
        ('THU', 'Jueves'),
        ('FRI', 'Viernes'),
        ('SAT', 'Sabado'),
        ('SUN', 'Domingo'),
    ]
    id_doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="available_times")
    id_office = models.ForeignKey(Office,on_delete=models.CASCADE,related_name="available_times")
    day = models.CharField(max_length=3,choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField()
    
    def __str__(self):
        return f"{self.id_doctor} - {self.day} from {self.start_time} to {self.end_time} at {self.id_office}"
    
class Citation(models.Model):
    id_patient = models.ForeignKey(Patient,on_delete=models.SET_NULL,null=True,related_name="citations")
    id_available_time = models.ForeignKey(Available_Times,on_delete=models.SET_NULL,null=True,related_name="citations")
    date = models.DateTimeField()
    status = models.CharField(max_length=10)
    comments = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"Cita para {self.id_patient} el {self.date} - Estado: {self.status}"
    
class Medical_History(models.Model):
    id_citation = models.ForeignKey(Citation,on_delete=models.SET_NULL, null=True ,related_name="medical_history")
    diagnostic = models.TextField()
    treatment = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Historial médico de cita {self.id_citation.id} - Estado: {'Activo' if self.status else 'Inactivo'}"
    
class Prescription(models.Model):
    id_medical_history = models.ForeignKey(Medical_History,on_delete=models.CASCADE,related_name="prescriptions")
    medicament = models.CharField(max_length=50)
    dose = models.TextField()
    instructions = models.TextField()
    date_issued = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='prescriptions_pdfs/', null=True, blank=True)
    
    def __str__(self):
        return f"Prescripcion para {self.id_medical_history.id_citation.id_patient} - {self.medicament}"
    
class File(models.Model):
    id_medical_history = models.ForeignKey(Medical_History,on_delete=models.CASCADE,related_name="files")
    name = models.CharField(max_length=150)
    route = models.FileField(upload_to='medical_files/', null=True,blank=True)
    date_uploaded = models.DateField()
    
    def __str__(self):
        return self.name