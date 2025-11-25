from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    truncated_bytes = password.encode("utf-8")[:72]
    truncated_password = truncated_bytes.decode("utf-8", errors="ignore")
    return pwd_context.hash(truncated_password)


def verify_password(password: str, hashed: str) -> bool:
    truncated = password.encode("utf-8")[:72]
    return pwd_context.verify(truncated, hashed)
