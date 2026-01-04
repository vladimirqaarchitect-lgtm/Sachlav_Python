cities_input = input("insert 5 cities spread with comma:")

cities = [city.strip() for city in cities_input.split(",")]

for i  in range(len(cities)):
    city = cities[i]
    output = f"City {i+1}: {city}"

    if "a" in city.lower():
        output += f" (This city name contains 'a')"

    print(output)


# London, Paris, Tokyo, NYC, Rome




