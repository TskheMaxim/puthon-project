students = {}
students["John"] = []
students["Anna"] = []

choice = input("Do u want to change data? (y/N): ").lower()

while choice == "y":

  name = input("Enter name: ")
  score = int(input("Enter score: "))

  if name not in students:
    add = input("Students not found. Add new student? (y/N): ")

    if add.lower() == "y":
      students[name] = [] #creates new student
    else:
      print("Canceled")
      choice = input("Do u want to continue? (y/N): ").lower()
      continue 

  students[name].append(score)



print(students) 
  
