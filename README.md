# DarwinAI

# Assistente Virtual: A Origem das Espécies

Este projeto desenvolve um assistente virtual baseado no modelo **Retrieval-Augmented Generation (RAG)** para responder a perguntas sobre o livro *A Origem das Espécies*, de Charles Darwin. A aplicação utiliza técnicas avançadas de NLP, como embeddings e bancos de dados vetoriais, para localizar informações relevantes no texto e também conta com uma busca na web para complementar as respostas com resumos e opiniões externas.

Além de oferecer uma versão interativa acessível via linha de comando, o projeto também disponibiliza uma interface web desenvolvida com Streamlit, permitindo que o assistente seja executado e testado de maneira intuitiva diretamente pelo navegador.

---

## Índice

- [Características](#características)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Uso](#uso)
  - [Execução via Linha de Comando](#execução-via-linha-de-comando)
  - [Execução via Streamlit (Interface Web)](#execução-via-streamlit-interface-web)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Observações Finais](#observações-finais)

---

## Características

- **Processamento do Texto:** O assistente carrega e analisa o conteúdo do arquivo *the Origin of Species.txt*, segmentando-o em partes otimizadas para pesquisa e recuperação de informações.
- **Banco de Dados Vetorial:** Utiliza embeddings gerados pela API da OpenAI e o FAISS para indexação e recuperação de trechos relevantes.
- **Pipeline RAG:** Implementa um fluxo de recuperação e resposta que combina a consulta do usuário com os dados extraídos do texto, apresentando respostas embasadas e as fontes consultadas.
- **Integração com a Web:** Para informações complementares, o assistente pode buscar resumos e opiniões na internet por meio da API Tavily.
- **Interface Alternativa:** Além da interação via terminal, há a opção de executar o assistente via Streamlit, proporcionando uma experiência mais acessível e interativa.

---

## Pré-requisitos

- **Python:** Versão 3.7 ou superior.
- **Dependências:** As bibliotecas necessárias estão listadas no arquivo `requirements.txt`.
- **API Keys:** São exigidas chaves de acesso válidas para a OpenAI e para o Tavily, que devem ser configuradas no arquivo `.env`.

---

## Instalação e Configuração

1. **Clone o Repositório**

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   cd <NOME_DO_DIRETÓRIO>

   ```

2. **Crie e Ative um Ambiente Virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows
   ```

3. **Instale as Dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração das Variáveis de Ambiente**

   ```
   OPENAI_API_KEY="SUA-CHAVE-API-DA-OPENAI-AQUI"
   TAVILY_API_KEY="SUA-CHAVE-API-DO-TAVILY-AQUI"
   ```

5. **Verifique os Arquivos do Projeto**

   Certifique-se de que os seguintes arquivos estão presentes:
   
   - `config.py` – Responsável pelo gerenciamento das variáveis de ambiente..
   - `main.py` – Contém a lógica interativa do assistente via terminal.
   - `rag_module.py` – Processa o texto, cria o banco de dados vetorial e estrutura o pipeline RAG.
   - `web_utils.py` – Inclui funções para busca na web e obtenção de resumos.
   - `the Origin of Species.txt` – Arquivo base contendo o conteúdo do livro.
   - *(Opcional)* Arquivo do **Streamlit** (ex.: `streamlit_app.py`) – Para executar a versão web da aplicação.

---

## Uso

### Execução via Linha de Comando

1. Abra o terminal no diretório do projeto.
2. Execute:

   ```bash
   python main.py
   ```

3. Siga as instruções na tela para interagir com o assistente.

### Execução via Streamlit (Interface Web)

1. Verifique se o arquivo do Streamlit (`streamlit_app.py`) está presente.
2. No terminal, execute:

   ```bash
   streamlit run streamlit_app.py
   ```

---

## Estrutura do Projeto

- **config.py:** Gerencia as variáveis de ambiente.
- **main.py:** Implementa o fluxo principal do assistente.
- **rag_module.py:** Contém funções para carregar e processar o texto, criar o banco de dados vetorial e configurar o pipeline RAG.
- **web_utils.py:** Permite busca na web e extração de resumos.
- **the Origin of Species.txt:** Arquivo base com o texto do livro.
- **requirements.txt:** Lista as bibliotecas necessárias.
- **.env:** Configuração das variáveis de ambiente.
- **(Opcional) streamlit_app.py:** Interface web.

---

## Observações Finais

- **Personalização:** Os parâmetros do assistente podem ser ajustados conforme necessário.
- **Contribuições:**  Pull requests são bem-vindos para melhorias no projeto.
- **Testes:** Recomenda-se testar tanto a versão via terminal quanto a interface web para avaliar a melhor experiência de uso.

---
