# name = "Donald Trump"

# print(name[1::2])
# print(name[::2])
#
#
# my_list = [1, 2, 3]
# for index, value in enumerate(my_list):
#     if index % 2 != 0:
#         print(f"index: {index}, value: {value}")

# new_name = name[-1] + name[:-1]
# print(new_name)

# text = "Manchester"

# print(text[-4:])
# print(text[0::2])
#
# message = (print(input("Enter a message:"))
# print(input("First character:"))
# print(input("Last character:"))
# print(input("Middle character:"))
# print(input("even Index:"))
# print(input("even Index character:"))
# print(input("odd Index character:"))
#
# print(input("odd Index character:"))

# # task 1
# name = "messi"
# age = 33
# print(f"hello {name}, yoa are {age} old")

# task 2

srt = input("Enter the text:")

print(srt.upper())
print(srt.lower())
print(srt.capitalize())
print(srt.title())
print(srt.split())


words = srt.split()

words.sort()

print("Alphabetically first word:", words[0])
print("Alphabetically last word:", words[-1])
