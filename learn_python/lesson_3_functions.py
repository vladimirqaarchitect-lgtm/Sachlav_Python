# def hello(name):
#     print("Hello World")
#     print("Hello there", name)
#
#
# hello("Bogdan")
# hello("Alice")
#
# def hello():
#     print("Hello World")
#
# hello()

def sum_nums(a, b):
    sum = a + b
    # print(sum)
    return sum


first_sum = sum_nums(10, 5)
print(first_sum)


print(sum_nums(sum_nums(50.5, 20), 30))

