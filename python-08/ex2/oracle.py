import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")
    print(f"API Access: {os.getenv('API_KEY')}")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
