from autogen import UserProxyAgent, ConversableAgent
from workflow import WorkFlow, BinaryWorkFlow
config = [{
    "model":"mistral",
    "base_url":"http://localhost:11434/v1",
    "api_key":"NULL"
}]

def get_data(boot):
    llm_config = {"config_list":config}
    prompt = [
       "You are a data formatter we have some data yes or no vary so output in boolean form (1 for Yes, 0 for No — boolean); and some data integer and float if you are given terms 'AGE' store INTEGER (not boolean) and Sex store if male then 0 and female then store 1 (boolean); hypertension, heart_disease, ever_married: 1=Yes, 0=No (boolean); work_type, smoking_status: label encoded ints (not boolean); residence_type: 0=Rural, 1=Urban (boolean); avg_glucose_level, bmi: float (not boolean), highChol (boolean), cholCheck (boolean), physActivity, fruits (boolean), veggies (boolean),hvyAlcohal(boolean), GenHlth(integer),menHlth (integer), physHlth(integer), diffWalk(boolean), highBP (boolean), Diabities(boolean) output -> 'age : 55years store 55? 2. What is your gender? store if male 0 othervise 1 (boolean)' 3. do you smoke ? if yes then store 1 otherwise 0 like boolean example store zero or one (boolean)",
       "You are a JSON generator who generates the json from key and store the output in integer format. For '1. What is your age[AGE]? 2. What is your sex?[SEX]' Output -> {'AGE': 55, 'SEX': 1} only the generated json format and show",
    
    ]
    work1 = BinaryWorkFlow(prompt,llm_config,1)
    data = work1.get_output(boot)
    print(data)
    return data

get_data("i do not smoke and my age 20 a male my heart disease no, bmi 35.7 and hypertension yes")