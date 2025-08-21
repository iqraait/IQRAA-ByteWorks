import csv
from django.core.management.base import BaseCommand
from front_office.models import Department, Doctor  # replace 'yourapp' with your app name


class Command(BaseCommand):
    help = "Import Departments and Doctors from CSV file (columns: name, department)"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)  # expects headers: name, department
            for row in reader:
                doctor_name = row.get("name", "").strip()
                dept_name = row.get("department", "").strip()

                if not doctor_name:
                    continue  # skip if doctor name missing

                # Create/get department
                dept = None
                if dept_name:
                    dept, _ = Department.objects.get_or_create(name=dept_name)

                # Create/get doctor
                doctor, created = Doctor.objects.get_or_create(
                    name=doctor_name,
                    defaults={"department": dept},
                )

                # If doctor exists but has no department or different one, update it
                if not created and dept and doctor.department != dept:
                    doctor.department = dept
                    doctor.save()

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added Doctor: {doctor.name} ({dept_name})"))
                else:
                    self.stdout.write(self.style.WARNING(f"Updated/Exists: {doctor.name} ({dept_name})"))
