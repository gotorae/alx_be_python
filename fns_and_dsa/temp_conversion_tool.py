FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(temp_fahrenheit):
    """Converts temperature in Fahrenheit to Celsius."""
    return (temp_fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(temp_celsius):
    """Converts temperature in Celsius to Fahrenheit."""
    return (temp_celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:
    try:
        temperature = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        continue

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature):.2f}°F")
        break
    elif unit == "F":
        print(f"{temperature}°F is {convert_to_celsius(temperature):.2f}°C")
        break
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
