# config.py
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Função auxiliar para obter uma variável de ambiente
def get_env_var(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"A variável de ambiente {var_name} não está definida.")
    return value

# Exemplo de acesso às chaves:
OPENAI_API_KEY = get_env_var("OPENAI_API_KEY")
TAVILY_API_KEY = get_env_var("TAVILY_API_KEY")
