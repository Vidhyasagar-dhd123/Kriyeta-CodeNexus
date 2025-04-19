import hashlib

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.email = email

        self.password =password

    def hash_password(self, password: str):
        """Hashes the password before storing it."""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.password = password
    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
    

