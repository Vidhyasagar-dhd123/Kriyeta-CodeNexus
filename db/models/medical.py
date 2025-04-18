class Medical:
    def __init__(self, user_id: int, medical_name: str, medical_description: str) -> None:
        self.user_id = user_id
        self.medical_name = medical_name
        self.medical_description = medical_description

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "medical_name": self.medical_name,
            "medical_description": self.medical_description
        }