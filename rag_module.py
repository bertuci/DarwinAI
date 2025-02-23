# rag_module.py
import os
import numpy as np
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

def load_and_process_text(file_path: str):
    """
    Carrega e processa o texto de um arquivo, dividindo-o em partes menores.
    """
    try:
        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # Tamanho ideal para embeddings
            chunk_overlap=200  # Sobreposição para contexto contínuo
        )
        return text_splitter.split_documents(documents)
    except Exception as e:
        print(f"Erro ao carregar ou processar o texto: {e}")
        return None

def create_vector_store(documents):
    """
    Cria um banco de dados vetorial usando embeddings da OpenAI.
    """
    try:
        embeddings = OpenAIEmbeddings()
        return FAISS.from_documents(documents, embeddings)
    except Exception as e:
        print(f"Erro ao criar o banco de dados vetorial: {e}")
        return None

def setup_rag_pipeline(vector_store):
    """
    Configura o pipeline RAG para responder perguntas.
    """
    try:
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", max_tokens=150)
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})
        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
    except Exception as e:
        print(f"Erro ao configurar o pipeline RAG: {e}")
        return None

def extract_semantic_keywords(query: str) -> str:
    """
    Extrai palavras-chave semânticas da consulta do usuário.
    """
    try:
        embeddings = OpenAIEmbeddings()
        query_embedding = np.array(embeddings.embed_query(query))
        relevant_terms = ["darwin", "seleção natural", "evolução", "espécies", "adaptação"]
        term_embeddings = [np.array(embeddings.embed_query(term)) for term in relevant_terms]
        
        keywords = [
            term for term, term_embedding in zip(relevant_terms, term_embeddings)
            if np.dot(query_embedding, term_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(term_embedding)) > 0.7
        ]
        return " ".join(keywords)
    except Exception as e:
        print(f"Erro ao extrair palavras-chave: {e}")
        return ""
