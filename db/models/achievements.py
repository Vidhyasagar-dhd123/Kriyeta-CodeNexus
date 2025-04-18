from datetime import datetime

class Achievement:
    def __init__(self, user_id, achievement_name:str,achivement_status:bool,createdAt:None):
        self.user_id = user_id
        self.achievement_name = achievement_name
        self.achivement_status =achivement_status
        createdAt = createdAt if createdAt else datetime.now(datetime.timezone.utc)

    def to_dict(self):
        return{
            "user_id":self.user_id,
            "achievement_name":self.achievement_name,
            "achievement_status":self.achivement_status,
            "createdAt": self.createdAt
        }
        