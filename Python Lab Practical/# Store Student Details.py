# Store Student Details

student = {
    "Name": input("Enter student name: "),
    "Roll No": input("Enter roll number: "),
    "Branch": input("Enter branch: "),
    "Semester": input("Enter semester: "),
    "Marks": input("Enter marks: ")
}

print("\nStudent Details")
print("-------------------")
print("Name:", student["Name"])
print("Roll No:", student["Roll No"])
print("Branch:", student["Branch"])
print("Marks:", student["Marks"])