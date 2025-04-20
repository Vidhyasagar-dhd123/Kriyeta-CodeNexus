from openai import OpenAI
from dotenv import load_dotenv
import os
from autogen import ConversableAgent

load_dotenv()

# client = OpenAI(base_url="https://beta.sree.shop/v1", api_key="ddc-beta-1dkh8ukdqe-67V4Mc9XhDzK0ILxBVVCkYlsIMHdfqrgA3r")

# completion = client.chat.completions.create(
#   model="Provider-9/gpt-4.1",
#   messages=[
#     {
#       "role": "user",
#       "content": "How are you",}]
  
# )

class MyBaseAgent(ConversableAgent):
    def generate_reply(self, messages=None, sender=None, config=None):
        # Remove invalid "name" fields
        for m in messages:
            if m.get("role") in ["user", "assistant"] and "name" in m:
                del m["name"]
        return super().generate_reply(messages=messages, sender=sender, config = config)
    def get_message(self):
        print(super().chat_messages)

