#  Python function that takes a list of numbers as input from the user and produces the corresponding cumulative list where each element in the list present at index i is the sum of elements at index j <= i
def cumulative_list(nums):
    cumul_list = []

    # Calculate the cumulative sum of the list.
    cumul_sum = 0
    for num in nums:
        cumul_sum += num
        cumul_list.append(cumul_sum)

    return cumul_list


# Get a list of numbers from the user.
num_str = input("Enter a list of numbers separated by spaces: ")
nums = [int(num) for num in num_str.split()]

# Calculate the cumulative list and print the result.
cumul = cumulative_list(nums)
print("The cumulative list is:", cumul)
