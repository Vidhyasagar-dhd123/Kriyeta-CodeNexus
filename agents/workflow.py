from autogen import ConversableAgent, GroupChat, GroupChatManager, UserProxyAgent, AssistantAgent

class WorkFlow():
    def __init__(self,prompt,llm_config,max_turns):
        self.planner_prompt = prompt[0]
        self.executor_prompt = prompt[1]
        self.validator_prompt = prompt[2]
        self.llm_config = llm_config
        self.max_turns = max_turns

    def get_output(self,boot):
        planner = ConversableAgent(
            "Planner",
            system_message=self.planner_prompt,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )
        executor = ConversableAgent(
            "Executor",
            system_message=self.executor_prompt,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )
        validator = ConversableAgent(
            "Validator",
            system_message=self.validator_prompt,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )
        
        result = planner.initiate_chat(executor,message=boot, max_turns= self.max_turns)
        final_result = executor.initiate_chat(validator,message=result.chat_history[-1]["content"], max_turns = self.max_turns)
        return final_result.chat_history[-1]["content"]
    
class BinaryWorkFlow():
    def __init__(self,prompt,llm_config,max_turns):
        self.planner_prompt = prompt[0]
        self.executor_prompt = prompt[1]
        self.llm_config = llm_config
        self.max_turns = max_turns
        self.history = []

    def get_output(self,boot):
        planner = ConversableAgent(
            "Planner",
            system_message=self.planner_prompt,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )
        executor = ConversableAgent(
            "Executor",
            system_message=self.executor_prompt,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )
        
        result = planner.initiate_chat(executor,message=boot, max_turns= self.max_turns)
        print(result)
        self.history.extend(result.chat_history)
        return result.chat_history[-1]["content"]
    
    def set_history(self,data):
        self.history.extend(data)

    def get_history(self):
        return self.history

class GroupedWorkFlow():
    def __init__(self,prompt,llm_config,max_turns):
        self.executor_prompt = prompt[0]
        self.llm_config = llm_config
        self.max_turns = max_turns
        self.history = []

    def get_output(self,boot):
        executor = AssistantAgent(
            "Executor",
            system_message=self.executor_prompt,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )

        user = UserProxyAgent(
            "user",
        )
        self.history = self.history[::-1]
        for h in self.history:
            if h["name"] == "Executor":
                executor.receive(h,sender=executor)
            else :
                executor.receive(h,sender=user)
        groupchat = GroupChat([executor],messages=self.history, max_round=1)
        manager = GroupChatManager(groupchat,"chat_manager",system_message="You are a chat manager.", human_input_mode="NEVER")
        result = manager.initiate_chat(executor,message=boot, max_turns= self.max_turns)
        self.history.extend(result.chat_history)
        return result.chat_history[-1]["content"]
    
    def set_history(self,data):
        self.history.extend(data)

    def get_history(self):
        return self.history
