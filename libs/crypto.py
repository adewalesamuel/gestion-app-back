from passlib import hash

def hash_password(password: str) -> str:
    return hash.sha256_crypt.encrypt(password)

def is_password(password: str, hashed_password: str) -> bool:
    return hash.sha256_crypt.verify(password, hashed_password)