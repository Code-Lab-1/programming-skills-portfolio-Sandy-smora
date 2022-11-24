# info 2.0
student = {
    "Name" : "Sandy Sarte", "Age" : 17, 
    "Class" : "Year1", "Gender" : "Female", "Location" : "Earth"
}

print(student["Location"])

print()

print(student.keys())
print(student.values())
print(student.items())

print()

student["Age"] = 18
print(student)

print()

student.update({"Blood Type" : "O"})
print(student)

print()

student.pop("Class")
print(student)

print()

len(student)