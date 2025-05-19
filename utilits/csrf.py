import secrets
from datetime import datetime, timedelta

__csrf_tokens = {} # Формат словаря: {"токен":"время_действия"}

def generate_csrf_token(expire_minutes: int = 10) -> str:
    """генерация токена"""
    token= secrets.token_urlsafe(32)
    expires = datetime.now() + timedelta(minutes=expire_minutes)
    __csrf_tokens[token]=expires.isoformat()
    return token

def validate_csrf_token(token: str) -> bool:
    """валидация токена"""
    if token not in __csrf_tokens:
        return False

    expires = datetime.fromisoformat(__csrf_tokens[token])
    if datetime.now() > expires:
        del __csrf_tokens[token]
        return False

    del __csrf_tokens[token]
    return True