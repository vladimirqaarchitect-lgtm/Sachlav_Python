my_list = list(range(1, 21))

odd_numbers = list(
    filter(lambda x: x % 2 != 0, my_list)
)

my_cubed_list = list(
    map(lambda x: x ** 3, odd_numbers)
)

print(my_cubed_list)

print(
    f"\nThe exact numbers in cubes: " + ", ".join(f"{x}^3" for x in odd_numbers))
