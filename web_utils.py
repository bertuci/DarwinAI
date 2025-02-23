# web_utils.py
import os
import requests
from bs4 import BeautifulSoup
from rag_module import extract_semantic_keywords

def search_web(query: str):
    """
    Pesquisa na web usando a API Tavily com base em conceitos semânticos.
    """
    try:
        keywords = extract_semantic_keywords(query)
        search_query = f"opiniões sobre {keywords} em A Origem das Espécies"
        url = "https://api.tavily.com/search"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('TAVILY_API_KEY')}"
        }
        data = {"query": search_query, "max_results": 3}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("results", [])
    except Exception as e:
        print(f"Erro ao pesquisar na web: {e}")
        return []

def extract_summary_from_url(url: str) -> str:
    """
    Extrai um resumo do conteúdo de uma página web.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = " ".join([p.get_text() for p in paragraphs])
        return content[:200] + "..." if len(content) > 200 else content
    except Exception as e:
        print(f"Erro ao extrair resumo da URL {url}: {e}")
        return "Resumo indisponível."
