#  Python function that takes n as an input and creates a list of n lists such that ith list contains first five multiples of i

def nlist(n):
          result = [[] for _ in range(n)]
          for i in range(1, n+1):
                    for j in range(1, 6):
                              result[i-1] = result[i-1] + [i*j]
          return result

print("The list is ", nlist(5) )

