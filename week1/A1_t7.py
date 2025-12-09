# Info message
print("Calculate fuel consumtion.\n")

# Ask for distance
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)

# Ask for fuel usage
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)

# Calculate consumption per 100 km
Consumption = int((FuelUsage / Distance) * 100)

# Print result
print(f"\nFuel consumption is {Consumption} l per 100 km")