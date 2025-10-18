class Student:
    def __init__(self, name, student_id, grade, attendance):
        self.name = name.title()  # Proper capitalization
        self.student_id = student_id.upper()  # Make ID uppercase
        self.grade = grade.upper()
        self.attendance = attendance

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Attendance: {self.attendance}%")


class ReportSystem:
    def __init__(self):
        self.reports = []

    def add_report(self, student, subject, marks):
        report = {
            "Student Name": student.name,
            "Student ID": student.student_id,
            "Subject": subject.title(),
            "Marks": marks
        }
        self.reports.append(report)
        print(f"✅ Report for {student.name} added successfully!")

    def show_reports(self):
        print("\n--- All Reports ---")
        if not self.reports:
            print("No reports found!")
        else:
            for report in self.reports:
                print(f"{report['Student Name']} ({report['Student ID']}) - {report['Subject']}: {report['Marks']} Marks")


class Portal:
    def __init__(self):
        self.students = []
        self.report_system = ReportSystem()

    def add_student(self):
        try:
            name = input("Enter student name: ").strip()
            student_id = input("Enter student ID: ").strip()
            grade = input("Enter grade: ").strip()
            attendance = float(input("Enter attendance percentage: "))  # numeric validation

            if not name or not student_id or not grade:
                raise ValueError("⚠️ All fields are required!")

            if attendance < 0 or attendance > 100:
                raise ValueError("⚠️ Attendance must be between 0 and 100.")

            student = Student(name, student_id, grade, attendance)
            self.students.append(student)
            print(f"✅ Student {student.name} added successfully!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("⚠️ Invalid input. Please try again.")

    def show_students(self):
        print("\n--- All Students ---")
        if not self.students:
            print("No students available!")
        else:
            for student in self.students:
                student.display_info()

    def add_report(self):
        student_id = input("Enter student ID for report: ").strip().upper()
        subject = input("Enter subject: ").strip().title()
        try:
            marks = int(input("Enter marks (0–100): "))
            if marks < 0 or marks > 100:
                raise ValueError("⚠️ Marks must be between 0 and 100.")
        except ValueError:
            print("⚠️ Please enter valid numeric marks.")
            return

        for student in self.students:
            if student.student_id == student_id:
                self.report_system.add_report(student, subject, marks)
                return
        print("⚠️ Student not found!")


def main():
    portal = Portal()
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Add Report")
        print("4. Show All Reports")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            portal.add_student()
        elif choice == '2':
            portal.show_students()
        elif choice == '3':
            portal.add_report()
        elif choice == '4':
            portal.report_system.show_reports()
        elif choice == '5':
            print("👋 Thank you for using Student Management System!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
