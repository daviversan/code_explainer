# AI Code Analyzer

Esse projeto consiste em um ambiente para colar código e receber uma resposta gerada por IA, explicando sua lógica. Esse sistema foi desenvolvido com Langchain utilizando o modelo llama3-8b-8192 conectado à Groq Cloud API e foi criado especificamente para o entendimento de questões de Estruturas de dados e algortimos do site Leetcode.

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/ai-code-analyzer.git](https://github.com/seu-usuario/ai-code-analyzer.git)
    cd ai-code-analyzer
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Defina sua chave de API como uma variável de ambiente:**
    ```bash
    export GROQ_API_KEY='sua_chave_api_do_groq' # No Windows: set GROQ_API_KEY=sua_chave_api_do_groq
    ```

5.  **Execute o aplicativo Flask:**
    ```bash
    python app.py
    ```

6.  Abra o arquivo `index.html` no seu navegador.