from autogen import UserProxyAgent, ConversableAgent, AssistantAgent
from .workflow import BinaryWorkFlow, GroupedWorkFlow
import os
config = [{
    "model":os.getenv("MODEL"),
    "base_url":os.getenv("BASE_URL"),
    "api_key":os.getenv("API_KEY")
}]

def check_data(boot,history):
    llm_config = {"config_list":config}
    prompt = [
       "You are a medical assistant who only assess user.",
    ]
    work1 = GroupedWorkFlow(prompt,llm_config,1)
    work1.set_history(history)
    data = work1.get_output(boot)
    return data, work1.history


def get_tool(query):
    assistant = AssistantAgent(
                "assistant",
                system_message="You are a vocabulary and json expert, choose the term from ['HYPERTENSION','DIABETES','ANOTHER'] which relates the best to the user query in form of json in less than 4 words.",
                llm_config={"config_list":config},
                human_input_mode="NEVER",
            )
    tool_data = assistant.generate_reply(messages=[{"role":"user","content":query}])
    return tool_data