from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(temperature=0)

def plan_tasks(user_input, memory):
    prompt = PromptTemplate(
        input_variables=["task"],
        template="Break the following task into 3-5 subtasks with priorities and suggested schedule:\n\nTask: {task}\n\nSubtasks:"
    )
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
    response = chain.run(user_input)
    return response.strip().split("\n")
