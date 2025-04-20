import os
import autogen

# Load config from environment
config_list = [{
    "model": os.getenv("MODEL"),
    "api_key": os.getenv("API_KEY"),
    "base_url": os.getenv("BASE_URL"),
}]

# Create assistant agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# Create user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config=False
)

# Store chat history as list of message dicts
history = []

print("💬 Start chatting with the assistant (type 'exit' to quit):")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ("exit", "quit"):
        print("👋 Chat ended.")
        break

    # Add user input to history
    history.append({"role": "user", "content": user_input})

    # Generate assistant's reply with full context
    reply = assistant.generate_reply(history, sender=user_proxy)

    # Add assistant's reply to history
    history.append({"role": "assistant", "content": reply})

    print("Assistant:", reply)
