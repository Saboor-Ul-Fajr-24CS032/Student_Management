import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from PIL import Image, ImageTk
import io
import requests

# ---------- Backend Classes (Your Original Logic) ----------
class Student:
    def __init__(self, name, student_id, grade, attendance):
        self.name = name.title()
        self.student_id = student_id.upper()
        self.grade = grade.upper()
        self.attendance = attendance

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

# ---------- Main Portal ----------
class Portal:
    def __init__(self):
        self.students = []
        self.report_system = ReportSystem()

    def add_student(self, name, student_id, grade, attendance):
        student = Student(name, student_id, grade, attendance)
        self.students.append(student)

    def add_report(self, student_id, subject, marks):
        for student in self.students:
            if student.student_id == student_id.upper():
                self.report_system.add_report(student, subject, marks)
                return True
        return False

portal = Portal()

#----------Background for everyone
def apply_background(self):
    try:
            url = "https://img.freepik.com/free-vector/hand-painted-watercolor-abstract-watercolor-background_23-2149008792.jpg"
            resp = requests.get(url, timeout=8)
            img = Image.open(io.BytesIO(resp.content)).convert("RGBA")
            img = img.resize((855, 555))
            self.images["bg"] = ImageTk.PhotoImage(img)

            bg_label = tk.Label(self.root, image=self.images["bg"])
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e :
            print("Background error:", e)
            self.root.config(bg="#FFE5B4")

# ---------- GUI ----------
class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("855x555")
        self.root.resizable(False, False)
        self.root.config(bg="#FFE5B4")  # pastel peach background

        self.screen1()

    # ---------- Screen 1 ----------
    def screen1(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if not hasattr(self, "images"):
            self.images = {}

    # Background Image
        apply_background(self)

    # School Logo
        try:    
            logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcUDNbO4zrc2UYLnVXS5mT_bwu9S_1M8YSmA&s"
            resp = requests.get(logo_url, timeout=8)
            img1 = Image.open(io.BytesIO(resp.content)).convert("RGBA")
            img1 = img1.resize((100, 100))
            self.images["logo"] = ImageTk.PhotoImage(img1)

            logo_label = tk.Label(self.root, image=self.images["logo"], bd=0)
            logo_label.place(x=378, y=30)
        except Exception as e :
            print("logo error:", e)
            pass    

    # Title
        title = tk.Label(self.root, text="School Management System", font=("Arial", 28, "bold"), 
                     fg="#FF7F50", bg="#FFE5B4")  # use valid bg color
        title.place(x=200, y=180)

    # Enter Button
        enter_btn = tk.Button(self.root, text="Enter", font=("Arial", 16), bg="#FF7F50", fg="white",
                          width=10, command=self.screen2)
        enter_btn.place(x=355, y=300)


    # ---------- Screen 2 (Dashboard) ----------
    def screen2(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        apply_background(self)

        # Buttons as Frames with Images & Text
        button_info = [
    ("Add Student", self.screen_add_student, "➕"),
    ("Show Students", self.screen_show_students, "📋"),
    ("Add Report", self.screen_add_report, "➕"),
    ("Show Reports", self.screen_show_reports, "📊")
]

    # Sizes & Spacing (Adjust these anytime)
        box_w = 370     # width of each box
        box_h = 200     # height of each box
        x_spacing = 30  # horizontal spacing between boxes
        y_spacing = 40  # vertical spacing at top & between rows
        top_margin = 45 # space before first row (Y axis)

        for index, (text, command, icon) in enumerate(button_info):
            row = index // 2
            col = index % 2

            x_pos = col * (box_w + x_spacing) + x_spacing
            y_pos = row * (box_h + y_spacing) + top_margin

            frame = tk.Frame(self.root, bg="#FFCC99", width=box_w, height=box_h, bd=3, relief="ridge")
            frame.place(x=x_pos, y=y_pos)

            frame.pack_propagate(False)
            frame.grid_propagate(False)

            label_icon = tk.Label(frame, text=icon, font=("Arial", 42, "bold"), bg="#FFCC99")
            label_icon.pack(pady=(20, 5))

            label_text = tk.Label(frame, text=text, font=("Arial", 18, "bold"), bg="#FFCC99")
            label_text.pack(pady=(0, 10))

            frame.bind("<Button-1>", lambda e, cmd=command: cmd_password(cmd))
            label_icon.bind("<Button-1>", lambda e, cmd=command: cmd_password(cmd))
            label_text.bind("<Button-1>", lambda e, cmd=command: cmd_password(cmd))

    # Exit Button with spacing under boxes
        exit_btn = tk.Button(self.root, text="Exit", font=("Arial", 14), bg="#FF6347", fg="white",
                     command=self.confirm_exit)
        exit_btn.place(x=720, y=510)
        

        # Password prompt wrapper
        def cmd_password(cmd):
            if cmd in [self.screen_add_student, self.screen_add_report]:
                pwd = simpledialog.askstring("Password Required", "Enter Password:", show="*")
                if pwd != "ALOHOMORA":
                    messagebox.showerror("Error", "Incorrect Password!")
                    return
            cmd()

    #------- to exit screen----
    def confirm_exit(self):
        ask = messagebox.askyesno("Confirm Exit", "Do you really want to exit?")
        if ask:
            self.root.quit()

    # ---------- Add Student ----------
    def screen_add_student(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        apply_background(self)

        tk.Label(self.root, text="Add Student", font=("Arial", 24, "bold"), bg="#FFE5B4").pack(pady=10)

        labels = ["Name", "ID", "Grade", "Attendance"]
        entries = {}
        for lbl in labels:
            frame = tk.Frame(self.root, bg="#FFE5B4")
            frame.pack(pady=5)
            tk.Label(frame, text=lbl+":", font=("Arial", 14), width=12, anchor="w", bg="#FFE5B4").pack(side="left")
            entry = tk.Entry(frame, font=("Arial", 14))
            entry.pack(side="left")
            entries[lbl] = entry

        def add_student_cmd():
            try:
                name = entries["Name"].get().strip()
                sid = entries["ID"].get().strip()
                grade = entries["Grade"].get().strip()
                att = float(entries["Attendance"].get())
                if not name or not sid or not grade:
                    raise ValueError("All fields are required!")
                if att < 0 or att > 100:
                    raise ValueError("Attendance must be 0-100!")
                portal.add_student(name, sid, grade, att)
                messagebox.showinfo("Success", f"Student {name} added successfully!")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except:
                messagebox.showerror("Error", "Invalid input!")

        tk.Button(self.root, text="Add", font=("Arial", 14), bg="#FF7F50", fg="white", command=add_student_cmd).pack(pady=20)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.screen2).pack()

    # ---------- Show Students ----------
    def screen_show_students(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        apply_background(self)
        tk.Label(self.root, text="All Students", font=("Arial", 24, "bold"), bg="#FFE5B4").pack(pady=10)

        # Scrollable Treeview
        columns = ("Name", "ID", "Grade", "Attendance")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        for stu in portal.students:
            tree.insert("", "end", values=(stu.name, stu.student_id, stu.grade, stu.attendance))
        tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.screen2).pack(pady=5)

    # ---------- Add Report ----------
    def screen_add_report(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        apply_background(self)

        tk.Label(self.root, text="Add Report", font=("Arial", 24, "bold"), bg="#FFE5B4").pack(pady=10)

        labels = ["Student ID", "Subject", "Marks"]
        entries = {}
        for lbl in labels:
            frame = tk.Frame(self.root, bg="#FFE5B4")
            frame.pack(pady=5)
            tk.Label(frame, text=lbl+":", font=("Arial", 14), width=12, anchor="w", bg="#FFE5B4").pack(side="left")
            entry = tk.Entry(frame, font=("Arial", 14))
            entry.pack(side="left")
            entries[lbl] = entry

        def add_report_cmd():
            try:
                sid = entries["Student ID"].get().strip()
                sub = entries["Subject"].get().strip()
                marks = int(entries["Marks"].get())
                if marks < 0 or marks > 100:
                    raise ValueError("Marks must be 0-100!")
                if portal.add_report(sid, sub, marks):
                    messagebox.showinfo("Success", f"Report added for {sid}")
                else:
                    messagebox.showerror("Error", "Student not found!")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except:
                messagebox.showerror("Error", "Invalid input!")

        tk.Button(self.root, text="Add", font=("Arial", 14), bg="#FF7F50", fg="white", command=add_report_cmd).pack(pady=20)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.screen2).pack()

    # ---------- Show Reports ----------
    def screen_show_reports(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        apply_background(self)
        tk.Label(self.root, text="All Reports", font=("Arial", 24, "bold"), bg="#FFE5B4").pack(pady=10)

        columns = ("Student Name", "Student ID", "Subject", "Marks")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        for rep in portal.report_system.reports:
            tree.insert("", "end", values=(rep["Student Name"], rep["Student ID"], rep["Subject"], rep["Marks"]))
        tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.screen2).pack(pady=5)


# ---------- Run ----------
root = tk.Tk()
app = StudentGUI(root)
root.mainloop()
