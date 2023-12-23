from django.core.management.base import BaseCommand
from csdstudentweb.models import Student

class Command(BaseCommand):
    help='Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_student()
        
    def create_student(self):
        student1 = Student(student_id="80018", last_name="Reyes", first_name="Maria Theresa", middle_name="Garcia",
                            birthdate="2002-12-13", gender="F", email="80018@psu.palawan.edu.ph", address="Tiniguiban", phone_number="093632112450")
        student2 = Student(student_id="80019", last_name="Lim", first_name="Roberto", middle_name="Alvaro",
                            birthdate="2001-06-18", gender="M", email="80019@psu.palawan.edu.ph", address="Sta. Monica", phone_number="09258778478")
        student3 = Student(student_id="80020", last_name="Aquino", first_name="Miguel", middle_name="",
                            birthdate="2002-04-25", gender="M", email="80020@psu.palawan.edu.ph", address="San Jose", phone_number="09125542178")
        student4 = Student(student_id="80021", last_name="Fernandez", first_name="Patricia", middle_name="dela Cruz",
                            birthdate="2003-01-12", gender="F", email="80021@psu.palawan.edu.ph", address="San Manuel", phone_number="09352874196")
        student5 = Student(student_id="80022", last_name="Santos", first_name="Rafael", middle_name="Abad",
                            birthdate="2003-03-03", gender="M", email="80022@psu.palawan.edu.ph", address="San Jose", phone_number="09365247815")
        student6 = Student(student_id="80023", last_name="Castro", first_name="Ana Marie", middle_name="dela Rosa",
                            birthdate="2001-12-31", gender="F", email="80023@psu.palawan.edu.ph", address="San Miguel", phone_number="09864282192")
        student7 = Student(student_id="80024", last_name="Ramos", first_name="Jose Luis", middle_name="Santos",
                            birthdate="2003-11-09", gender="M", email="80024@psu.palawan.edu.ph", address="Sicsican", phone_number="09138429281")
        student8 = Student(student_id="80025", last_name="Dizon", first_name="Angelica", middle_name="Ocampo",
                            birthdate="2002-08-21", gender="F", email="80025@psu.palawan.edu.ph", address="Irawan", phone_number="09364415284")
        student9 = Student(student_id="80026", last_name="Diaz", first_name="Jane", middle_name="",
                            birthdate="2002-04-13", gender="F", email="80026@psu.palawan.edu.ph", address="Tanglaw", phone_number="09345668255")
        student10 = Student(student_id="80027", last_name="Mayer", first_name="John", middle_name="",
                            birthdate="2002-07-28", gender="M", email="80027@psu.palawan.edu.ph", address="Bagong Sikat", phone_number="09052789435")
        
        student_detail= [student1, student2, student3, student4, student5, student6, student6, student7, student8, student9, student10]
        for student in student_detail:
            student.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully created student detail.'))
        print(f"Student record count: {Student.objects.count()}")