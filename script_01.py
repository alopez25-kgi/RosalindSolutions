with open('notes.txt', 'r') as file:
lines = file.readlines()
print(lines)
print(len(lines))
print(lines[0].strip())
