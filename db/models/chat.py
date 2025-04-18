class Chat:
    def __init__(self, user_mail:str,query:str, response:str):
        self.usermail = user_mail
        self.query = query,
        self.response = response

    def to_dict(self):
        return {
            "user_mail": self.usermail,
            "query": self.query,
            "response": self.response
        }