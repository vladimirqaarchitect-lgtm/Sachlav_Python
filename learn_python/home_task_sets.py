my_set = {1, 2, 4, 6, 'a', 'b', 'c'}

my_set.add(200)

other_set = {9, 12, 45, 200, 'a', 'b', 'c'}

common_elements_set = set(my_set) & set(other_set)

print(list(common_elements_set))