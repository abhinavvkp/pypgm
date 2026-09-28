students = {
    "Anu":85,
    "Rahul":90,
    "Asha":85,
    "Meera":95
}
print("Original Dictionary:")
print(students)
sorted_students = sorted(
    students.items(),
    key=lambda x:(x[1],x[0])
)
print("Sorted Dictionary:")
print(dict(sorted_students))