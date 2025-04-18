from autogen import ConversableAgent

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
        return result.chat_history[-1]["content"]

