def garden_operations(error_idx: int) -> None:
    """
    test 4 types of errors
    ValueError, ZeroDivisionError, FileNotFoundError and KeyError
    and then all together

    error_idx: index of each error test case and all together
    """
    if error_idx.__class__.__name__ != "int":
        return
    match error_idx:
        case 0:
            print("\nTesting ValueError...")
            print(int("abc") + 35)
        case 1:
            print("\nTesting ZeroDivisionError...")
            print(10/0)
        case 2:
            print("\nTesting FileNotFoundError...")
            fd = open("missing.txt", "r")
            fd.close()
        case 3:
            print("\nTesting KeyError...")
            my_dic = {'a': 1, 'b': 2}
            print(my_dic['missing_plant'])
        case 4:
            print("\nTesting multiple errors together...")
            print(int("abc") + 35)
            print(10/0)
            fd = open("missing.txt", "r")
            fd.close()
            my_dic = {'a': 1, 'b': 2}
            print(my_dic['missing_plant'])


def test_error_types() -> None:
    """
    test all types of errors
    """
    try:
        garden_operations(0)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        garden_operations(1)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        garden_operations(2)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        garden_operations(3)
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    try:
        garden_operations(4)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
