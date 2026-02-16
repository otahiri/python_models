import sys


def main() -> None:
    current = sys.prefix
    base = sys.base_prefix
    print(base)
    print(current)
    # to check if you are inside a Virtual environment you need to compare
    # prefix and base prefix if they are the same then you are not inside a
    # Virtual environment else you are inside a Virtual environment
    if current == base:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current}")
        print("Virtual Environment:  None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {current}")
        print("Virtual Environment: matrix_env")
        print(f"Environment Path: {current}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(f"{current}/lib/python3.11/site-packages")


if __name__ == "__main__":
    main()
