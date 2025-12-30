def garden_operations(error_idx: int):
    """
    test 4 types of errors
    ValueError, ZeroDivisionError, FileNotFoundError and KeyError
    and then all together

    error_idx: index of each error test case and all together
    """
    match error_idx:
        case 0:
            print("\nTesting ValueError...")
            try:
                print(int("abc") + 35)
            except ValueError:
                print("Caught ValueError: invalid literal for int()")
        case 1:
            print("\nTesting ZeroDivisionError...")
            try:
                print(10/0)
            except ZeroDivisionError:
                print("Caught ZeroDivisionError: division by zero")
        case 2:
            print("\nTesting FileNotFoundError...")
            try:
                fd = open("missing.txt", "r")
                print(fd.read())
            except FileNotFoundError:
                print("Caught FileNotFoundError: No such file 'missing.txt'")
        case 3:
            print("\nTesting KeyError...")
            my_dic = {'a': 1, 'b': 2}
            try:
                print(my_dic['missing_plant'])
            except KeyError:
                print("Caught KeyError: 'missing\_plant'")
        case 4:
            print("\nTesting multiple errors together...")
            try:
                print(int("abc") + 35)
            except ValueError:
                pass
            try:
                print(10/0)
            except ZeroDivisionError:
                pass
            try:
                fd = open("missing.txt", "r")
                print(fd.read())
            except FileNotFoundError:
                pass
            my_dic = {'a': 1, 'b': 2}
            try:
                print(my_dic['missing_plant'])
            except KeyError:
                pass
            print("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)
    print("\nAll error types tested successfully!")


test_error_types()
