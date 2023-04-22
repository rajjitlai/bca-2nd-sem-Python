# Implementation of Binary search technique

list_num = [12, 13, 14, 17, 18, 19]
print("The list is: ", list_num)

x = int(input("Enter the number to be searched: "))

low = 0
high = len(list_num) - 1

while low <= high:
    mid = (low + high) // 2
    if list_num[mid] == x:
        print(f"{x} is found at position {mid}")
        break
    elif list_num[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(f"{x} is not in {list_num}")
