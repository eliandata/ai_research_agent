from duckduckgo_search import DDGS
from agents import function_tool

@function_tool
def web_search(query: str) -> str:
    """
    Perform a web search using DuckDuckGo and return the first results.

    Args:
        query (str): Query to perform the search.

    Returns:
        str: List of titles and excerpts from the search results.
    """
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        if not results:
            return "No results found.."
        return "\n".join(f"- {r['title']}: {r['body']}" for r in results)


