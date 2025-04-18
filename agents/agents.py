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
       "You are a question generator if you are given terms 'AGE' and 'NAME' output -> '1. What is your age[AGE]? 2. What is your name?[NAME]'",
       "You are a JSON generator who generates the json from questions. For '1. What is your age[AGE]? 2. What is your name?[NAME]' Output -> {'AGE': 'What is your age?', 'NAME':'What is your name?'}",
       ""
    ]
    work1 = WorkFlow(prompt,llm_config,1)
    data = work1.get_output(boot)
    print(data)
    return data

get_data("Generate questions for a medical diagnosis for following points : 'AGE'->int, 'STROKE'->'Yes or No'")