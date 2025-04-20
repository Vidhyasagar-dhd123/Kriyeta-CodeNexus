from autogen import ConversableAgent
import os
from model_loader import get_pred_diabetes
config = [{
    "model":os.getenv("MODEL"),
    "base_url":os.getenv("BASE_URL"),
    "api_key":os.getenv("API_KEY")
}]
# Let's first define the assistant agent that suggests tool calls.
assistant = MyBaseAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with simple calculations. "
    "Return 'TERMINATE' when the task is done.",
    llm_config={"config_list":config},
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# Register the tool signature with the assistant agent.
assistant.register_for_llm(name="calculator", description="A simple calculator")(get_pred_diabetes)

# Register the tool function with the user proxy agent.
user_proxy.register_for_execution(name="calculator")(get_pred_diabetes)

chat_result = user_proxy.initiate_chat(assistant, message="The data is float 1.0 for all fields there are 17 fields in the argument")