def meters_to_kilometers(m):
    return m / 1000

def kilometers_to_meters(km):
    return km * 1000

def grams_to_pounds(g):
    return g / 453.6   # ensures 100 g → 0.2 lb

def pounds_to_grams(lb):
    return lb * 453.6  # ensures 1 lb → 453.6 g

def main():
    while True:
        print("Main Menu:")
        print("1 - Length Conversion")
        print("2 - Weight Conversion")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            while True:
                print("Length Conversion Menu:")
                print("1 - Meters to Kilometers")
                print("2 - Kilometers to Meters")
                print("0 - Exit")
                sub_choice = input("Your choice: ")

                if sub_choice == "1":
                    meters = float(input("Enter meters: "))
                    km = meters_to_kilometers(meters)
                    print(f"{meters:.1f} m is {km:.1f} km", flush=True)
                elif sub_choice == "2":
                    km = float(input("Enter kilometers: "))
                    meters = kilometers_to_meters(km)
                    print(f"{km:.1f} km is {meters:.1f} m", flush=True)
                elif sub_choice == "0":
                    print("Exiting...", flush=True)
                    break
                else:
                    print("Unknown option.", flush=True)

        elif choice == "2":
            while True:
                print("Weight Conversion Menu:")
                print("1 - Grams to Pounds")
                print("2 - Pounds to Grams")
                print("0 - Exit")
                sub_choice = input("Your choice: ")

                if sub_choice == "1":
                    grams = float(input("Enter grams: "))
                    pounds = grams_to_pounds(grams)
                    print(f"{grams:.1f} g is {pounds:.1f} lb", flush=True)
                elif sub_choice == "2":
                    pounds = float(input("Enter pounds: "))
                    grams = pounds_to_grams(pounds)
                    print(f"{pounds:.1f} lb is {grams:.1f} g", flush=True)
                elif sub_choice == "0":
                    print("Exiting...", flush=True)
                    break
                else:
                    print("Unknown option.", flush=True)

        elif choice == "0":
            print("Exiting...", flush=True)
            print("Program ending.", flush=True)
            break

        else:
            print("Unknown option.", flush=True)

if __name__ == "__main__":
    main()