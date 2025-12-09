def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    while True:
        print("Options:")
        print("1 - Celsius to Fahrenheit")
        print("2 - Fahrenheit to Celsius")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            try:
                celsius = float(input("Insert the amount of Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.1f} °C equals to {fahrenheit:.1f} °F", flush=True)
            except ValueError:
                print("Invalid input. Please enter a number.", flush=True)

        elif choice == "2":
            try:
                fahrenheit = float(input("Insert the amount of Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.1f} °F equals to {celsius:.1f} °C", flush=True)
            except ValueError:
                print("Invalid input. Please enter a number.", flush=True)

        elif choice == "0":
            print("Exiting...", flush=True)
            break
        else:
            print("Unknown option.", flush=True)

if __name__ == "__main__":
    main()
