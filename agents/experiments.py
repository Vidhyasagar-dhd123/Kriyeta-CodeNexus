from workflow import GroupedWorkFlow

config = [{
    "model":"mistral",
    "base_url":"http://localhost:11434/v1",
    "api_key":"NULL"
}]
prompt = [
       "You are a message checker if message related to medical or greeting then output -> Yes otherwise No along with the question"\
       "If user asks 'tell me about politics -> then reply = No [tell me about politics]'"\
       "If user asks Is stress a symptom to hypertension -> then reply = Yes[Is stress a symptom to hypertension] also add the additional information provided.",
       "If response contains yes then the user is asking valid question so answer using the data the user if response is no then make user ask another question and do not answer. tell user you are a medical assistant."
       "Example : If user asks 'tell me about cricket' then reply = I can not assist you with that.",
    ]
gwf = GroupedWorkFlow(prompt,{"config_list":config},max_turns=1)
gwf.set_history({"role":"user","content":"My name is vidhyasagar"})
print(gwf.get_output("What is my name"))