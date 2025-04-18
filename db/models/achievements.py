from datetime import datetime, timezone

class Achievement:
    def __init__(self, user_id, achievement_name: str, achievement_status: bool, createdAt=None):
        # If createdAt is not provided, use the current UTC time.
        self.user_id = user_id
        self.achievement_name = achievement_name
        self.achievement_status = achievement_status
        self.createdAt = createdAt if createdAt else datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "achievement_name": self.achievement_name,
            "achievement_status": self.achievement_status,
            "createdAt": self.createdAt,  # This stores the actual datetime object
        }

    def formatted_created_at(self):
        # This method returns the formatted string, but does not change the actual 'createdAt' field in the DB.
        return self.createdAt.strftime('%Y-%m-%d %H:%M:%S')
