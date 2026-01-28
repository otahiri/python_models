import sys


def main() -> None:
    """
    collect data from user the print each message in the correct channel
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    name = input("\nInput Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print(f"\n[STANDARD] Archive status from {name}: {status}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels \
verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
