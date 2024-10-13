from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_tavily(name: str):
     
    search = TavilySearchResults()
    res = search.run(f"{name}")
    
    return res
