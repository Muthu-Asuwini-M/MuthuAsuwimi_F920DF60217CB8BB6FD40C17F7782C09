class student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda  student: student.cgpa, reverse=True)
  return sorted_students 
students = [
  student("Iswariya","111",5.1),
  student("Santhiya","112",6.1),
  student("pradeeba","113",7.1),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {},Roll Number:{},CGPA: {}".format(student.name,student.roll_number,student.cgpa))