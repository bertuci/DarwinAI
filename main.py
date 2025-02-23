# main.py
import os
from config import OPENAI_API_KEY  # Apenas para garantir que as credenciais sejam carregadas
from rag_module import load_and_process_text, create_vector_store, setup_rag_pipeline
from web_utils import search_web, extract_summary_from_url

def main():
    """
    Função principal que executa o assistente virtual.
    """
    print("=== Assistente Virtual Baseado em 'A Origem das Espécies' ===")
    file_path = r"the Origin of Species.txt"
    
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        return
    
    # Carregar e processar o texto
    documents = load_and_process_text(file_path)
    if not documents:
        return
    
    # Criar o banco de dados vetorial
    vector_store = create_vector_store(documents)
    if not vector_store:
        return
    
    # Configurar o pipeline RAG
    rag_pipeline = setup_rag_pipeline(vector_store)
    if not rag_pipeline:
        return
    
    # Loop de interação com o usuário
    while True:
        user_input = input("\nDigite sua pergunta (ou 'sair' para encerrar): ").strip()
        if user_input.lower() in ["sair", "exit"]:
            print("Encerrando o assistente. Até logo!")
            break
        
        try:
            result = rag_pipeline.invoke({"query": user_input})
            answer = result["result"]
            source_documents = result["source_documents"]
            
            # Exibir resposta e fontes únicas
            print("\nResposta:")
            print(answer)
            print("\nFontes utilizadas:")
            unique_sources = set(doc.metadata['source'] for doc in source_documents)
            for source in unique_sources:
                print(f"- {source}")
            
            # Opção para buscar opiniões na web
            user_choice = input("\nGostaria de ver opiniões de outros leitores? (sim/não): ").strip().lower()
            if user_choice == "sim":
                print("\nBuscando opiniões na internet...")
                search_results = search_web(user_input)
                
                if search_results:
                    print("\nOpiniões encontradas:")
                    for idx, result in enumerate(search_results, start=1):
                        title = result.get("title", "Sem título")
                        url = result.get("url", "#")
                        summary = extract_summary_from_url(url)
                        print(f"{idx}. {title}")
                        print(f"   Resumo: {summary}")
                        print(f"   Link: {url}")
                else:
                    print("Nenhuma opinião encontrada.")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")

if __name__ == "__main__":
    main()
