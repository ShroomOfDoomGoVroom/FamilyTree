# initialize necessary vars
rela = {}
with open("relationships.txt", "r") as f:
  data = f.read()
  if data != "":
    data = data.split("\n")
    for line in data:
      if line == "":
        continue
      keyVal = line.split(",")
      keyVal = [int(i) for i in keyVal]
      key = keyVal[0]
      val = keyVal[1:]
      rela[key] = val

# Function for adding a new name
def add_new(name):
  with open("names.txt", 'r') as f:
    data = f.read()
  with open("names.txt", 'a') as f:
    if data != "":
      last = data.split("\n")[-2]
      number = int(last.split(',')[-1]) + 1
    else:
      number = 0
    f.write(name + "," + str(number) + "\n")
    rela[number] = []
  return number

# Function for finding the corresponding name
def find_name(number):
  with open("names.txt", 'r') as f:
    data = f.read()
    lines = data.split("\n")
    for line in lines:
      stored = line.split(",")
      if int(stored[1]) == number:
        return stored[0]
    return "Not Found"

# Find the number of a name
def find_number(name):
  with open("names.txt", 'r') as f:
    data = f.read()
    lines = data.split("\n")
    for line in lines:
      stored = line.split(",")
      if stored[0] == name:
        return int(stored[1])
    return -1

# add a new relationship between numbers
def new_rela(parent, child):
  rela[parent].append(child)

# print out children of a number
def show_children(parent):
  print()
  printing = True
  parent_list = [parent]
  parents = len(parent_list)
  children_list = rela[parent]
  all_children = children_list[:]
  num_children = [len(children_list)]
  for parent in parent_list:
      print(find_name(parent), end="\t")
  while printing:
    parents = len(parent_list)
    print()
    for _ in range(3):
      print(("|\t"*parents))
    for num in num_children:
      print(num, end="\t")
    print()
    for child in all_children:
      print(find_name(child), end='\t')
    parent_list = all_children
    all_children = []
    num_children = []
    for parent in parent_list:
      children_list = rela[parent]
      all_children.extend(children_list)
      num_children.append(len(children_list))
    if all_children == []:
      printing = False


#Initialize variables
names = []
choosing = True


#Infinite Loop
while choosing == True:
  action = input("""Do you want to 
1 - add a new family member
2 - draw your family tree
3 - clear the existing family tree
4 - exit program: \n""")
  print()
  while action not in ["1", "2", "3", "4", "5"]:
    action = input("""Do you want to 
1 - add a new family member
2 - draw your family tree
3 - clear the existing family tree
4 - exit program: \n""")
        
  if action == "1":
    name = input("Enter a name: ")
    names.append(name)
    number = add_new(name)
    parent = input("This is the child of: ")
    if parent == "":
      continue
    parent_num = find_number(parent)
    if parent_num != -1:
      new_rela(parent_num, number)

  if action == "2":
    head = input("Who is the head of the family: ")
    while find_number(head) == -1:
      head = input("Who is the head of the family: ")
    show_children(find_number(head))
    print()

  if action == "3":
    with open("names.txt", "w") as f:
      f.close()
    with open("relationships.txt", "w") as f:
      f.close()
    print("The family tree has been erased.")
  if action == "4":
    with open("relationships.txt", "w") as f:
      f.close()
    with open("relationships.txt", "a") as f:
      for key in rela:
        f.write("\n" + str(key))
        for val in rela[key]:
          f.write(","+str(val))
    choosing = False
