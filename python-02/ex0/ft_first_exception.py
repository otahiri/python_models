def check_temperature(temp_str):
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
        print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        if temp_str.isdigit() and 40 < int(temp_str) < 0:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
            return
        print(f"Error: '{temp_str}' is not a valid number")


check_temperature("abs")
