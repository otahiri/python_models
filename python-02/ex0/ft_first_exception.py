def check_temperature(temp_str):
    """
    check if temperature is ok for plants to live in

    temp_str: the temperature in a string format
    """
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if 40 < temp or temp < 0:
            raise ValueError
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    except ValueError:
        if all(n.isdigit() for n in temp_str):
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
            return
        elif temp_str[0] == "-" and any(not n.isdigit() for n in temp_str):
            print(f"Error: {temp_str}°C is too cold for plants (max 40°C)")
            return
        print(f"Error: '{temp_str}' is not a valid number")


print("=== Garden Temperature Checker ===")
check_temperature("25")
check_temperature("abc")
check_temperature("100")
check_temperature("-50")
print("\nAll tests completed - program didn't crash!")
