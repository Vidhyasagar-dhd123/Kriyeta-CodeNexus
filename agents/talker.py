from autogen import UserProxyAgent, ConversableAgent
from .workflow import BinaryWorkFlow, GroupedWorkFlow

config = [{
    "model":"mistral",
    "base_url":"http://localhost:11434/v1",
    "api_key":"NULL"
}]

def check_data(boot,history=None):
    llm_config = {"config_list":config}
    prompt = [
       "You are a message checker if message related to medical or greeting then output -> Yes otherwise No along with the question"\
       "If user asks 'tell me about politics -> then reply = No [tell me about politics]'"\
       "If user asks Is stress a symptom to hypertension -> then reply = Yes[Is stress a symptom to hypertension] also add the additional information provided.",
       "If response contains yes then the user is asking valid question so answer using the data the user if response is no then make user ask another question and do not answer. tell user you are a medical assistant."
       "Example : If user asks 'tell me about cricket' then reply = I can not assist you with that.",
    ]
    work1 = GroupedWorkFlow(prompt,llm_config,1)
    if history:
        work1.set_history(history)
    data = work1.get_output(boot)
    print(data)
    return data, work1.history
