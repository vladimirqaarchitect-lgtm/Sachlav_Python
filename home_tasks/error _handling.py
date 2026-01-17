data = {"price": "10.5", "id": "abc"}


def get_as_float(data_dict, key):
    try:
        value = data_dict[key]
        number = float(value)
        print(f"Success: the number {number} have gotten")
        return number
    except KeyError:
        print(f"The key {key} was not found in the data")

    except ValueError:
        print(f"Error: The value for key '{key}' can't be converted to float!")



print(get_as_float(data, "price"))   # успех
print(get_as_float(data, "id"))      # ValueError
print(get_as_float(data, "amount"))