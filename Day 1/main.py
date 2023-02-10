def band_name():
    print("Welcome to the Band Name Generator.")

    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")

    return(f"Your band name could be {city} {pet}")

print(band_name())