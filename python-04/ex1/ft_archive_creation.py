def main() -> None:
    """
    print entries in a file to store the info
    """
    name = "new_discovery.txt"
    entries = """
[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("\nInitializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")
    try:
        catalog = open(name, "w")
        catalog.write(entries)
        print(entries)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{name}' ready for long-term preservation.")
        catalog.close()
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        print("Warning: invalid file or file not found")


if __name__ == "__main__":
    main()
