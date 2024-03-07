import autogen

llm_config = {
    "config_list": [
        {"model":"gpt-4",
         "api_key": "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"}],
    "temperature": 0.9,
    "timeout": 300,
}

assistant = autogen.AssistantAgent(name="assistant", llm_config=llm_config)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir":"web","use_docker": False},
    llm_config=llm_config,
    system_message=""""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
My Skills are as follows:1) Coding 2) Communication 3) Sports. Save these in a .png file format  
"""
user_proxy.initiate_chat(
    assistant,
    message=task
)

# task2 = """
# I think autogen is better
# """

# user_proxy.send(
#     recipient = assistant,
#     message = task2
# )