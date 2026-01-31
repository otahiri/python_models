def main() -> None:
    """
    print info from ancient_fragment
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    print("Connection established...")
    print("\nRECOVERED DATA:")
    try:
        fd = open("ancient_fragment.txt", "r")
        print(fd.read())
        fd.close()
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        print("ERROR: Storage vault not found. Run data generator first.")
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
