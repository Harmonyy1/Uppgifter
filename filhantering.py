while True:
    try:
        name = input("Filename: ")
        file = open(name, "w")
    except FileNotFoundError:
        print("")

