from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(BaseModel):
    GENDER_CHOICES =(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    student_id = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=1, null=False, blank=False, choices = GENDER_CHOICES)
    email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        full_name = f"{self.first_name} {self.middle_name} {self.last_name}".strip()
        return f"{full_name} - {self.student_id}"