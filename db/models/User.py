import hashlib

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, password: str):
        """Hashes the password before storing it."""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
