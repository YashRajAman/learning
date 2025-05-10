from langchain_openai import ChatOpenAI

from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.tools import tool
from csv_loader import get_collection
from env import anthropic_api_key

checkpointer = InMemorySaver()
store = InMemoryStore()



# 🔹 1. Define LLM with API Key, Base URL, and Model Name
LLM_API_KEY = "sk-no-key-required"  # Replace with actual API key
LLM_BASE_URL = "http://127.0.0.1:8080/v1"  # Adjust accordingly
LLM_MODEL_NAME = "mistral-7B-instruct"  # Replace with model name

model = ChatOpenAI(
    base_url=LLM_BASE_URL,
    api_key=LLM_API_KEY,
    model_name=LLM_MODEL_NAME,
    model_kwargs={"functions": True}
)

#==========================RAG=====================
collection = get_collection()

@tool
def search_vectordb(query):
    """Search the vector database using the query."""
    results = collection.search(query)
    print(results)
    return results


query_agent = create_react_agent(
    model=model,
    tools=[search_vectordb],
    name="query_agent",
    prompt=("You are an assistant that must always use the `search_vectordb` tool "
        "to retrieve information from the database. "
        "Do not generate answers on your own. "
        "If the tool returns no data, respond with 'No data found.' "
        "Always return the source name when providing information.")

 )


# Create specialized agents

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    print("Tool calling.")
    return a * b

def web_search(query: str) -> str:
    """Search the web for information."""
    return (
        "Here are the headcounts for each of the FAANG companies in 2024:\n"
        "1. **Facebook (Meta)**: 67,317 employees.\n"
        "2. **Apple**: 164,000 employees.\n"
        "3. **Amazon**: 1,551,000 employees.\n"
        "4. **Netflix**: 14,000 employees.\n"
        "5. **Google (Alphabet)**: 181,269 employees."
    )

math_agent = create_react_agent(
    model=model,
    tools=[add, multiply],
    name="math_expert",
    prompt="You are a math expert. Always use one tool at a time."
)

research_agent = create_react_agent(
    model=model,
    tools=[web_search],
    name="research_expert",
    prompt="You are a world class researcher with access to web search. Do not do any math."
)

# Create supervisor workflow
workflow = create_supervisor(
    [research_agent, math_agent, query_agent],
    model=model,
    output_mode="full_history",
    prompt=(
        "You are a team supervisor managing a research expert and a math expert. "
        "For current events, use research_agent. "
        "For math problems, use math_agent."
        "For query related to document/files/customer info, use query_agent"
    )
)

# Compile and run
app = workflow.compile(checkpointer=checkpointer, store=store)

config = {"configurable": {"thread_id": "12345"}}

result = app.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Query agent, Please provide the details for the customer with the ID 'CFC6056BC2C3B0c' "
        }
    ]
}, config=config)

print(result)

