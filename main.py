###- initialize necessary vars -###
# dictionary that sotres all relationships
rela = {}
# load stored relationships from file
with open("relationships.txt", "r") as f:
  data = f.read()
  if data != "":
    data = data.split("\n")
    for line in data:
      if line == "":
        continue
      keyVal = line.split(",")
      # list comprehension to typecast all values in the list
      keyVal = [int(i) for i in keyVal]
      key = keyVal[0]
      val = keyVal[1:]
      rela[key] = val

###- function for adding a new name -###
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

###- function for finding the corresponding name -###
def find_name(number):
  with open("names.txt", 'r') as f:
    data = f.read()
    lines = data.split("\n")
    for line in lines:
      stored = line.split(",")
      if int(stored[1]) == number:
        return stored[0]
    return "Not Found"

###- find the number of a name -###
def find_number(name):
  with open("names.txt", 'r') as f:
    data = f.read()
    lines = data.split("\n")
    for line in lines:
      stored = line.split(",")
      if stored == []:
        return -1
      if stored[0] == name:
        return int(stored[1])
    return -1

###- add a new relationship between numbers -###
def new_rela(parent, child):
  rela[parent].append(child)

###- print out children of a number -###
def show_tree(parent):
  print()
  # setup to loop through
  printing = True
  # list of all parents
  parent_list = [parent]
  # children of one parent (this is only for the head)
  children_list = rela[parent]
  # list of all children
  all_children = children_list[:]
  # number of children of each parent
  num_children = [len(children_list)]
  print("----------")
  # print name of the head
  for parent in parent_list:
    print(find_name(parent), end="\t")

  # loop until it reaches the end
  while printing:
    # number of parents
    parents = len(parent_list)
    print()
    
    # print arrows
    for _ in range(3):
      print(("|\t"*parents))
    
    # print how many children each parent has
    for num in num_children:
      print(num, end="\t")
    print()

    # print all children
    for child in all_children:
      print(find_name(child), end='\t')

    # the children becomes parents
    parent_list = all_children
    all_children = []
    num_children = []

    # now get children of each new parent and store them
    for parent in parent_list:
      children_list = rela[parent]
      all_children.extend(children_list)
      num_children.append(len(children_list))
    
    # if list is empty, we have reached the end
    if all_children == []:
      printing = False
  print("\n----------\n")

# Initialize variables
choosing = True


# Infinite Loop
while choosing:
  action = input("""Do you want to:
1 - add a new family member
2 - draw your family tree
3 - clear the existing family tree
4 - exit program
> """)
  print()
  while action not in ["1", "2", "3", "4", "5"]:
    action = input("""Do you want to:
1 - add a new family member
2 - draw your family tree
3 - clear the existing family tree
4 - exit program
> """)
        
  if action == "1":
    name = input("Enter a name: ")
    if name != "":
      number = add_new(name)
      # make new relationship
      parent = input("This is the child of: ")
      if parent == "":
        continue
      parent_num = find_number(parent)
      if parent_num != -1:
        new_rela(parent_num, number)
    print()

  if action == "2":
    head = input("Who is the head of the family: ")
    while find_number(head) == -1:
      head = input("Who is the head of the family: ")
    show_tree(find_number(head))
    print()

  if action == "3":
    with open("names.txt", "w") as f:
      f.close()
    with open("relationships.txt", "w") as f:
      f.close()
    rela = {}
    print("The family tree has been erased.")
  
  if action == "4":
    with open("relationships.txt", "w") as f:
      f.close()
    with open("relationships.txt", "a") as f:
      for key in rela:
        f.write(str(key))
        for val in rela[key]:
          f.write(","+str(val))
        f.write("\n")
    choosing = False

  if action == "5":
    print(rela)
