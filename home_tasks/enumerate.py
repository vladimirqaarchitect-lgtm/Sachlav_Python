inventory = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'kiwi']

processed_items = []

for index, fruit in enumerate(inventory, start=1):

    if index % 2 == 0 and len(processed_items) > 5:
        processed_items.append(f" {index} long {fruit}")

    elif index % 2 != 0 and fruit[0] in ('a', 'e', 'i', 'o', 'u'):
        processed_items.append(f"{index}. Стартует с гласной: {fruit}")

    else:
        processed_items.append(f"{index}.{fruit})")

print("Исходный список inventory:")
print(inventory)

print("\nОбработанный список processed_items:")
print(processed_items)