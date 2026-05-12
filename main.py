import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7,
)

pesquisador = Agent(
    role="Pesquisador Sênior de Tecnologia",
    goal="Descobrir informações relevantes e atualizadas sobre {tema}",
    backstory=(
        "Você é um pesquisador experiente, conhecido por sua "
        "capacidade de identificar tendências e sintetizar informações "
        "complexas de forma clara."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

escritor = Agent(
    role="Redator Técnico",
    goal="Escrever um artigo claro e envolvente sobre {tema} com base na pesquisa",
    backstory=(
        "Você é um redator técnico que transforma informações densas "
        "em conteúdo acessível, mantendo precisão e fluidez."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

tarefa_pesquisa = Task(
    description=(
        "Pesquise os principais aspectos sobre {tema}. "
        "Identifique 5 pontos-chave: contexto, tendências atuais, "
        "desafios, oportunidades e perspectivas futuras."
    ),
    expected_output=(
        "Um relatório estruturado em bullet points com os 5 aspectos, "
        "cada um com 2-3 frases explicativas."
    ),
    agent=pesquisador,
)

tarefa_escrita = Task(
    description=(
        "Com base na pesquisa, escreva um artigo de blog sobre {tema}. "
        "O artigo deve ter introdução, 3-4 seções e conclusão."
    ),
    expected_output=(
        "Artigo em markdown, ~600 palavras, tom profissional mas acessível."
    ),
    agent=escritor,
    context=[tarefa_pesquisa],
)

crew = Crew(
    agents=[pesquisador, escritor],
    tasks=[tarefa_pesquisa, tarefa_escrita],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    tema = input("Tema do artigo: ").strip() or "Agentes de IA em 2026"
    resultado = crew.kickoff(inputs={"tema": tema})
    print("\n" + "=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)
    print(resultado)
