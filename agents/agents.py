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
        "You are a data collector who collects data by generating questions. Generate the questions in single line. For Example if the points are 'AGE'->int, 'STROKE'->'Yes or No'"
        "Give the question like '1. What is your age?[AGE] 2. Have you ever had a stroke.[STROKE]'",
        "You are a question validator who checks whether the question is related to the diagnosis of patient. If yes return the questions related to medical."
        "Give the question like '1. What is your age?[AGE] 'INT' 2. Have you ever had a stroke.[STROKE]'BOOL''",
        "You are a JSON expert who generates json using questions. For example if the question is 1. What is your age?[AGE] 'INT' 2. Have you ever had a stroke.[STROKE]'BOOL'"
        "Output -> {'AGE':'What is your age?','STROKE':'Have you ever had a stroke?'}"
    ]
    work1 = WorkFlow(prompt,llm_config,1)
    data = work1.get_output(boot)
    print(data)
    return data

get_data("Generate questions for a medical diagnosis for following points : 'AGE'->int, 'STROKE'->'Yes or No'")