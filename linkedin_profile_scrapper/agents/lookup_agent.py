import os
from dotenv import load_dotenv

load_dotenv()
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain.agents import create_react_agent , AgentExecutor
from langchain import hub
from tools.tools import get_profile_tavily


def lookup(name: str) -> str:

    llm = ChatOllama (
        temperature=0,
        model='llama3.2:1b'

    )

    template = '''
     given the full name of {person} I want you to get me a link to their Linkedin profile page. Answer should contail url only.
    '''

    prompt_template = PromptTemplate(
        template=template , input_variables=['person']
    )

    tool_for_agent = [
        Tool(
        name='linkedin web scraper and summarizer',
        func='?',
        description='useful for when you need to get the Linkedin Page URL',
        function = get_profile_tavily,

    )
    
    ]

    react_prompt = hub.pull('hwchase17/react')

    agent = create_react_agent(llm=llm , tools=tool_for_agent , prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent , tools=tool_for_agent , verbose=True)

    result = agent_executor.invoke(
        input={'input': prompt_template.format_prompt(person = name)}
    )

    url = result['output']

    return url

if __name__ == '__main__':
    url = lookup('Advait Shinde')
    print(url)


