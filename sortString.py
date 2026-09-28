strings = ["Python","C","Java","Programming","Ai"]
print("Orginal List:")
print(strings)
strings.sort(key=lambda x:len(x))
print("Sorted by Length:")
print(strings)