from config import Config
from security.encryption import SecureData

def main():
    print("🚀 GMPX-PRO V1 Starting...")

    secure = SecureData(Config.SECRET_KEY)

    sample = "Gold Signal: BUY"
    encrypted = secure.encrypt(sample)

    print("Encrypted:", encrypted)

    decrypted = secure.decrypt(encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
