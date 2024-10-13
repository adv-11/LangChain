from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama 
from langchain_core.output_parsers import StrOutputParser

from linkedin.linkedin import scrape_linkedin_profile

if __name__ == '__main__':

    

    summary_template = '''
    Given Linkedin  information {info} about a person , please create a short summary and 2 interesting facts about them.

'''
 
    prompt = PromptTemplate( input_variables=['info'] , template= summary_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url= 'https://www.linkedin.com/in/advait-shinde/'
    )

    llm = ChatOllama(model="llama3.2:1b")

    chain = prompt | llm | StrOutputParser()

    result = chain.invoke(input={'info' : linkedin_data})

    print(result)


