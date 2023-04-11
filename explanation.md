# Introduction to Python Programming

We will explore some simple Python programs that cover the basic syntax and control flow constructs in Python. We are going to learn about the Python Programs given in the syllabus of <b> BCA 2nd Semester </b>

## Explanation of [star.py](./2-printPatterns/star.py)

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

## Explanation of [num.py](./2-printPatterns/num.py)



