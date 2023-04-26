# Introduction to Python Programming

We will explore some simple Python programs that cover the basic syntax and control flow constructs in Python. We are going to learn about the Python Programs given in the syllabus of <b> BCA 2nd Semester </b>

<hr>

## Explanation of [star.py](./02-printPatterns/star.py)

Here's how the program works:

1. The number of rows in the pattern is set to 4 using the `rows` variable.

2. A variable named `k` is initialized to `2 * rows - 2`. This value is used to keep track of the number of spaces that need to be printed before each row of stars.

3. The function then uses a `for` loop to iterate through each row of the pattern.

4. In each iteration of the loop, the function first prints the required number of spaces using a nested `for` loop that iterates `k` times.

5. The value of `k` is decreased by 2 to account for the decreasing number of spaces required for each subsequent row.

6. A second nested `for` loop is used to print the required number of stars for that row.


7. Finally, the function prints a newline character to move to the next line.

8. Once the `printPattern` function is defined, the program calls it to print the pattern in the console.
<hr>

## Explanation of [num.py](./02-printPatterns/num.py)

Here's how the program works:

1. The number of rows in the pattern is set to 5 using the `rows` variable.

2. The function uses a `for` loop to iterate through each row of the pattern.

3. In each iteration of the loop, the function prints the required number of spaces using a nested `for` loop that iterates `rows-i` times.

4. The function then prints the required sequence of numbers for that row using two additional nested `for` loops. The first `for` loop iterates from `i` to `2*i-1` and prints the sequence of numbers in increasing order. The second `for` loop iterates from `2*i-2` to `i-1` in reverse order and prints the sequence of numbers in decreasing order.

5. Finally, the function prints a newline character to move to the next line and start printing the next row.

6. Once the `patternPrint` function is defined, the program calls it to print the pattern in the console.
<hr>

## Explanation of [mtheg.py](./03-mathexample/mtheg.py)

Here's how the program works:

1. The program first imports the `math` module using the `import` statement.

2. The program then calculates the square root of the number 25 using the `math.sqrt()` function and assigns the result to the `sqrt` variable. The program prints the result to the console.

3. The program then calculates the factorial of the number 5 using the `math.factorial()` function and assigns the result to the `fact` variable. The program prints the result to the console.

4. The program then converts the angle 45 degrees to radians using the `math.radians()` function and assigns the result to the `rad` variable. The program prints the result to the console.

5. The program then calculates the sine of the angle `pi/4` radians using the `math.sin()` function and assigns the result to the `sin` variable. The program prints the result to the console.

6. The program then calculates the cosine of the angle `pi/4` radians using the `math.cos()` function and assigns the result to the `cos` variable. The program prints the result to the console.

7. The program then calculates the logarithm base 10 of the number 1000 using the `math.log10()` function and assigns the result to the `log10` variable. The program prints the result to the console.
<hr>

## Explanation of [area.py](./04-area/area.py)

Here's how the program works:

1. First, we import the `math` module which provides access to various mathematical functions and constants.

2. We define a function `triArea()` which takes no arguments.

3. We get the length of three sides of a triangle as input from the user using `input()` function, and store them in variables `side1`, `side2`, and `side3`. We convert the input to float data type as the lengths of the sides can be in decimal form.

4. We use Python's `assert statement` to check that the input lengths of the triangle form a valid triangle. The assert statement will raise an exception if the condition is not True.

5. We calculate the semi-perimeter of the triangle as `(side1 + side2 + side3) / 2`. The semi-perimeter is half of the perimeter of the triangle.

6. We calculate the area of the triangle using Heron's formula which is given as `area = sqrt(s * (s - side1) * (s - side2) * (s - side3))`. Here, s is the semi-perimeter of the triangle.

7. Finally, we print the calculated area of the triangle using the `print()` function.
<hr>

## Explanation of [sales.py](./05-sales/sales.py)

Here's how the program works:

1. First, we define a function `salesReport` which takes a list salesRecord as input. This list contains the sales made by a salesman in a month.

2. We use the built-in `sum` function to calculate the total sales made by the salesman. The total sales are stored in the variable `totalSales`.

3. We use `conditional statements` to determine the remarks for the salesman based on their total sales. If the total sales are greater than or equal to 80000, the remarks are "Excellent". If the total sales are greater than or equal to 60000, the remarks are "Good". If the total sales are greater than or equal to 40000, the remarks are "Average". Otherwise, the remarks are "Work Hard".

4. We use another `conditional statement` to calculate the commission for the salesman based on their total sales. If the total sales are greater than or equal to 50000, the commission is calculated as 5% of the total sales. Otherwise, the commission is 0.

5. We return the total sales, commission, and remarks as a `tuple`.

6. We create a list `salesRecord` which contains the sales made by the salesman in a month.

7. We call the `salesReport` function with `salesRecord` as an argument and store the returned values in the variables `totalSales`, `commission`, and `remarks`.

8. We print the total sales and commission using the `print function`.

9. We use `conditional statements` to print a message based on the remarks of the salesman. If the remarks are "Excellent", we print "Great job! You exceeded your sales target.". If the remarks are "Good", we print "Well done! You made good sales this month.". If the remarks are "Average", we print "Good effort! Keep working to improve your sales.". Otherwise, we print "You need to work harder to meet your sales targets.".
<hr>

## Explanation of [factorial.py](./06-factorial/factorial.py)

Here's how the program works:

1. The program prompts the user to enter a number using the `input()` function with a message "Enter a number: ".

2. The user input is stored in a variable named `user_input` after converting it to an integer data type using the `int()` function.

3. The program defines a function named `factorial` that takes an integer `n` as input.

4. Inside the `factorial()` function, a variable named `fact` is initialized to 1.

5. The function then uses a `for` loop to iterate over each integer in the range from 1 to `n + 1`.

6. During each iteration, the value of `fact` is multiplied by the current integer.
7. Once the loop is complete, the final value of `fact` is the factorial of the input integer.

8. The program then calls the `factorial()` function with the `user_input` integer as an argument to calculate its factorial.

9. Finally, the program prints the value of the calculated factorial using an f-string with the message "The factorial of {user_input} is [factorial_value]".
<hr>

## Explanation of [fibo.py](./07-fibonacci/fibo.py)

Here's how the program works:

1. The user is prompted to enter a number using the `input()` function, and the input is stored in the variable `user_input`.

2. The `int()` function is used to convert the user input from a string to an integer.

3. The `fibonacci()` function is defined, which takes a single parameter `n` to specify the number of terms of the Fibonacci series to generate.

4 .The `a` and `b` variables are initialized to 0 and 1, respectively, which represent the first two terms of the series.

5. The first two terms of the series, i.e., 0 and 1, are printed using the `print()` function.

6. The `for` loop starts from index 2 and runs up to `n-1`.

7. In each iteration of the loop, the current term of the series is calculated as the sum of the previous two terms and stored in the variable `c`.

8. The value of `a` is updated to `b`, and the value of `b` is updated to `c`.

9. The current term `c` is printed using the `print()` function.

10. Finally, the `fibonacci()` function is called with the input value `user_input`, and the function generates and prints the Fibonacci series up to `user_input` terms.number.
<hr>

## Explanation of [revSum.py](./08-revSum/revSum.py)

Here's how the program works:

1. The user is prompted to enter a number with two or more digits using the `input()` function, and the input is stored in the variable `user_input`.

2. The `revSum()` function is defined to reverse the input number and calculate the sum of its digits.

3. The input number is reversed by converting it to a string using `str()` and then slicing it with `[::-1]`, which reverses the string.

4. A variable `sum` is initialized to 0 to hold the sum of the reversed number's digits.

5. A `for` loop is used to iterate through each digit of the reversed number. In each iteration, the current digit is converted to an integer using `int()` and added to the `sum` variable.

6. The reversed number and its `sum` are printed using the `print()` function.

7. The `revSum()` function is called to reverse the input number and calculate the sum of its digits.
<hr>

## Explanation of [lcmHcf.py](./09-lcmHcf/lcmHcf.py)

Here's how the program works:

1. The user is prompted to enter two numbers using the `input()` function, and the inputs are stored in the variables `userInput1` and `userInput2` as integers using `int()`.

2. The `lcmHcf()` function is defined to calculate the least common multiple (LCM) and highest common factor (HCF) of the two input numbers.

3. Two variables `big` and `small` are initialized to hold the larger and smaller of the two input numbers, respectively, using the `max()` and `min()` functions.

4. A `while` loop is used to repeatedly calculate the HCF of the two numbers, until the smaller number becomes zero. In each iteration, the smaller number is stored in a temporary variable `temp`, the remainder of `big` divided by `small` is calculated using the modulo operator `%`, and `big` is set to `temp`. The final value of `big` is the HCF of the two input numbers.

5. The LCM of two numbers is calculated as the product of the two numbers divided by their HCF, which is stored in the variable `lcm`.

6. The LCM and HCF of the two input numbers are printed using f-strings, which allow variables to be interpolated directly into a string.

7. The `lcmHcf()` function is called to calculate the LCM and HCF of the two input numbers.

8. The output displays the LCM and HCF of the two input numbers.
<hr>

## Explanation of [prime.py](./10-primeornot/prime.py)

Here's how the program works:

1. The `math` module is imported to use the `sqrt()` function.

2. A function named `is_prime()` is defined to determine whether the given number is prime or not.

3. The function takes one parameter `n` which is the number to be checked.

4. If `n` is less than 2, it is not considered as a prime number, and the function prints "`n` is not a prime number".

5. If `n` is 2, it is considered as a prime number, and the function prints "`n` is a prime number".

6. If `n` is an even number, it is not considered as a prime number, and the function prints "`n` is not a prime number".

7. If `n` is not an even number, then the function checks if it is divisible by any odd number between 3 and square root of `n`, inclusively. If it is, the function prints "`n` is not a prime number" and exits the loop using `break` statement. Otherwise, the function prints "`n` is a prime number".

8. The `is_prime()` function is called by passing `userInput` as an argument to check whether it is a prime number or not.

9. The output displays whether `userInput` is a prime number or not based on the result of `is_prime()` function.
<hr>


## Explanation of [ser1sum.py](./11-seriessum/ser1sum.py)

Here's how the program works:

1. First of all, we define a function called `sum_of_series()` that takes two arguments `n` and `x`.

2. The function calculates the sum of a series based on the given input values of `n` and `x` using a nested loop.

3. The function initializes some variables before the loop: `k` is set to 2, `sum` is initially set to 1, `sign` is set to 1 and `m` is set to 2.

4. The outer loop runs from 1 to `n` inclusive.

5. Within the outer loop, there is an inner loop that runs from 1 to `m` inclusive.

6. Within the inner loop, a variable called `fact` is calculated as the factorial of `m`.

7. After calculating `fact` in the inner loop, the `sign` is inverted using the `-sign` operation.

8. The sum of the series is then udpated by adding to it the value of the current term, which is calculated as `((x^k)/fact)*sign`.

9. The values of `k` and `m` are then incremented by 2 to prepare for the next iteration of the loop.

10. Finally, the function returns the total sum of the series.
<hr>

## Explanation of [ser2sum.py](./11-seriessum/ser2sum.py)

Here's how the code works:

1. The code defines a function called `series_sum` that takes two arguments, `n` and `x`.

2. The function initializes two variables: `k` is set to 2 and `sum` is initially set to 1.

3. The function uses a `for` loop to iterate over the even values between 2 and `n` inclusive.

4. Within the loop, a variable called `fact` is calculated as the factorial of the current even value.

5. The sum of the series is then updated by adding to it the value of the current term, which is calculated as `((x^i)/fact)`.

6. The function returns the total sum of the series.

7. The code calls the `series_sum` function with the input values of `n` and `x` (5 and 2, respectively) and assigns the result to a variable called `result`.

8. The code prints the value of `result`.
<hr>

