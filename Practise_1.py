# task_1 perform basic arithmetic operations of +, *, / on 2 given numbers
a = 6
b = 3

print(f"Addition = {a+b}")
print(f"Subtraction = {a-b}")
print(f"Multiplication = {a*b}")

# task_2 calculate result of a complex arithmetics expression

x = 100
y = 100
print(f"Expression = {x-(y/(1+x*y))}")

# task_3 find the average of two numbers in two different ways, -the regular average ag the geometric average

avr = (x + y)/2
avr_g = (x * y) ** 0.5

print(f"The average of a, b is equal to {avr}")
print(f"The geometric average of a, b is equal to {avr_g}")

# task_4 Calculate the longest side(hypotenuse) and the area of a triangle, using the lengths of the two sides

 # right triangle:

a = 3
b = 4
c = (a*a + b*b) ** 0.5
S = (a * b)/2

print(f"The length of hypotenuse is equal to {c}")
print(f"The square of triangle is equal to {S}")