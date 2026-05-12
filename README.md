# CrewAI - Sistema Multi-Agente

Exemplo: **Pesquisador + Escritor** colaborando para produzir um artigo.

## Setup

```bash
# 1. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar chave de API
copy .env.example .env
# edite .env e cole sua chave de console.anthropic.com

# 4. Rodar
python main.py
```

## Como funciona

- `pesquisador` coleta informações sobre o tema
- `escritor` recebe o resultado e produz o artigo
- `Process.sequential` garante que rodem em ordem
- O parâmetro `context=[tarefa_pesquisa]` passa o output da pesquisa para a escrita

## Próximos passos

- Adicionar ferramentas (`crewai_tools`): busca web, leitura de PDF, etc.
- Trocar `Process.sequential` por `Process.hierarchical` com um manager
- Adicionar mais agentes (revisor, editor, fact-checker)
