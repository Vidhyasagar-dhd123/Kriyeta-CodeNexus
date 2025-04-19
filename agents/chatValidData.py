from autogen import UserProxyAgent, ConversableAgent
from .workflow import WorkFlow
import os
config = [{
    "model":os.getenv("MODEL"),
    "base_url":os.getenv("BASE_URL"),
    "api_key":os.getenv("API_KEY")
}]

def check_data(boot):
    llm_config = {"config_list":config}
    prompt = [
       "You are a message checker if message related to medical or greeting then Yes othervise No",
       "If response is yes then the user is asking valid question so answer the user if response is no then make user ask another question. and tell user you are a medical assistant.",
       "You are a message updator update the message and return user friendly response in only one single line."
    ]
    work1 = WorkFlow(prompt,llm_config,1)
    data = work1.get_output(boot)
    print(data)
    return data
