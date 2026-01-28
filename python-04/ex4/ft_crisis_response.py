def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as fd:
            print(fd.read())
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as fd:
            print(fd.read())
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    archive = ""
    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as fd:
            archive = fd.read()
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        print("Warning file invalid or not found")
    print(f"SUCCESS: Archive recovered - ``{archive}''")
    print("STATUS: Normal operations resumed")
    print("\nAll crisis scenarios handled successfully. Archives secure")


if __name__ == "__main__":
    main()
