# Implementation of Linear search technique

list_num = [14, 12, 18, 19, 13, 17]
print("The list is: ", list_num)
x = int(input("Enter the number to be searched: "))
found = False
for i in range(len(list_num)):
          if(list_num[i] == x):
                    found = True
                    print(f"{x} is found at position{i}")
                    break

if found == False:
          print(f"{x} is not in {list_num}")