class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

  def __str__(self):
    return f"{self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"


def sort_students(student_list):
  # Sort the student_list in descending order based on CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Test the function with different input lists of students
if __name__ == "__main__":
  # Create a list of student objects
  students = [
      Student("Alice", "A123", 3.8),
      Student("Bob", "B456", 3.9),
      Student("Charlie", "C789", 3.5),
      Student("David", "D101", 3.7),
  ]

  # Sort the students by CGPA
  sorted_students = sort_students(students)

  # Print the sorted list
  for student in sorted_students:
    print(student)
