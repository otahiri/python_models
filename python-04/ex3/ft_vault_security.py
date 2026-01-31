def main() -> None:
    """
    main function of the program
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\nSECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as data:
            print(data.read())
    except (IsADirectoryError, PermissionError, FileNotFoundError):
        print("Warning: invalid file or file not found")
    try:
        print(("\nSECURE PRESERVATION:"))
        with open("security_protocols.txt", "w") as vault:
            vault.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
    except (IsADirectoryError, PermissionError, FileNotFoundError):
        print("Warning: invalid file or file not found")
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
