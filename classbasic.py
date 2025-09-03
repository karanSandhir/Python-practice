class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # A list containing marks in 5 subjects
        
    def average_marks(self):
        return sum(self.marks) / len(self.marks)
    
    def percentage(self):
        total_marks = sum(self.marks)
        max_total_marks = len(self.marks) * 100  # Assuming each subject is out of 100
        return (total_marks / max_total_marks) * 100
    
    def display_details(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.average_marks():.2f}")
        print(f"Percentage: {self.percentage():.2f}%")

# Example usage
marks = [85, 90, 78, 88, 92]
student = Student(101, "John Doe", marks)

# Displaying details
student.display_details()
