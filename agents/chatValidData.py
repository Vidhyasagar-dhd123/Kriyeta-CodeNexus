from autogen import UserProxyAgent, ConversableAgent
from workflow import WorkFlow
config = [{
    "model":"mistral",
    "base_url":"http://localhost:11434/v1",
    "api_key":"NULL"
}]

def get_data(boot):
    llm_config = {"config_list":config}
    prompt = [
       "you are a planner your work is to check the data is related to medical or health issue or greeting message if is it then generate the output 'Yes' and if not then generate 'No' ",
       "example data 'How are you??' -> 'Yes' 'i am nervous' -> 'No",
       "give the response according to given data",
       "example data 'How are you??' -> 'Yes' 'i am nervous' -> 'No",
       "genrate the response if 'No' "
    ]
    work1 = WorkFlow(prompt,llm_config,1)
    data = work1.get_output(boot)
    print(data)
    return data

get_data("Hey how are you?")