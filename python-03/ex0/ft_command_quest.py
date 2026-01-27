import sys

if __name__ == "__main__":
    len = len(sys.argv)
    print("=== Command Quest ===")
    if len == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len > 1:
        print(f"Arguments received: {len - 1}")
    count = 1
    for arg in sys.argv[1:]:
        print(f"Argument {count}: {sys.argv[count]}")
        count += 1
    print(f"Total arguments: {len}")
