from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "last_name", "first_name", "middle_name", "birthdate", "gender", 
                    "email", "address", "phone_number")
    search_fields = ("student_id",)