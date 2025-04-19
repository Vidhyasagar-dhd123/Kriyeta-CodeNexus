from bson import encode

class Chat:
    def __init__(self, user_mail:str,query:str, response:str,summary:dict):
        self.usermail = user_mail
        self.query = query,
        self.response = response
        self.summary = summary

    def to_dict(self):
        return {
            "user_mail": self.usermail,
            "query": self.query,
            "response": self.response,
            "summary": encode(self.summary) if self.summary else None
        }