import os
from typing import TypedDict, Literal
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# 🔹 1. Define LLM with API Key, Base URL, and Model Name
LLM_API_KEY = "sk-no-key-required"  # Replace with actual API key
LLM_BASE_URL = "http://127.0.0.1:8080/v1"  # Adjust accordingly
LLM_MODEL_NAME = "gpt-4"  # Replace with model name

llm = ChatOpenAI(
    base_url=LLM_BASE_URL,
    api_key=LLM_API_KEY
)

# 🔹 2. Define a Simple Tool for the Agent
@tool
def repeat_tool(text: str) -> str:
    """Repeats the user input."""
    return f"You said: {text}"

# 🔹 3. Create the RAG Agent
checkpointer = MemorySaver()
chat_agent = create_react_agent(model=llm, tools=[repeat_tool], checkpointer=checkpointer)

# 🔹 4. Define State for Conversation
class ChatState(TypedDict):
    messages: list
    next: Literal["agent", "end"]

# 🔹 5. Define Chat Node
def chat_node(state: ChatState):
    """Handles chat responses and updates history."""
    messages = state["messages"]
    
    # Get response from agent
    response = chat_agent.invoke({"messages": messages})
    
    # Append AI response to conversation history
    messages.append({"role": "assistant", "content": response["messages"][-1].content})
    
    return {"messages": messages, "next": "agent"}  # Continue chat

# 🔹 6. Build the StateGraph Chatbot
builder = StateGraph(ChatState)
builder.add_node("agent", chat_node)
builder.set_entry_point("agent")
chatbot = builder.compile(checkpointer=checkpointer)

# 🔹 7. Run the Chatbot
thread_id = "user_123"
messages = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Chat ended.")
        break
    
    messages.append({"role": "user", "content": user_input})

    for output in chatbot.stream(
        {"messages": messages}, config={"configurable": {"thread_id": thread_id}}
    ):  
        print(output)
        response = output["messages"][-1].content
        print(f"AI: {response}")
        messages.append({"role": "assistant", "content": response})
