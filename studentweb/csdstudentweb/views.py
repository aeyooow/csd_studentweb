from typing import Any
from django.shortcuts import render
from csdstudentweb.models import Student
from csdstudentweb.forms import StudentForm

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
import json

class HomePageView(ListView):
    model = Student
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StudentListView(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'students.html'
    # json_file_path = 'path to json file'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     student_data = self.get_student_data()
    #     context['student_data'] = student_data
    #     return context
    
    # def get_student_data(self):
    #     with open(self.json_file_path, 'r') as file:
    #         data = json.load(file)
    #         return data.get('students', [])

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student-list')