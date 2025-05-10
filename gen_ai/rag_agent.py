import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_openai import ChatOpenAI
from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.tools import tool
from typing import List
from env import anthropic_api_key
import os

class PDFEmbeddingStore:
    """A class to embed a PDF file into ChromaDB and manage its vector store."""
    
    def __init__(
        self,
        pdf_path: str,
        collection_name: str = "pdf_embeddings",
        chroma_persist_dir: str = "./chroma_db",
    ):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at {pdf_path}")
        
        self.pdf_path = pdf_path
        self.collection_name = collection_name
        self.chroma_persist_dir = chroma_persist_dir
        
        self.embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.client = chromadb.PersistentClient(path=self.chroma_persist_dir)
        self.collection = None
        self.documents = None
        self.vectorstore = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embedding_model,
            persist_directory=self.chroma_persist_dir,
        )
    
    def load_pdf(self) -> List:
        loader = PyPDFLoader(file_path=self.pdf_path)
        self.documents = loader.load()
        return self.documents
    
    def create_embeddings(self) -> None:
        if not self.documents:
            self.load_pdf()
        
        texts = [doc.page_content for doc in self.documents]
        embeddings = self.embedding_model.embed_documents(texts)
        
        self.collection = self.client.get_or_create_collection(name=self.collection_name)
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=[f"doc_{i}" for i in range(len(texts))]
        )
        
        self.vectorstore = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embedding_model,
            persist_directory=self.chroma_persist_dir,
        )
        print(f"Embeddings created and stored in collection '{self.collection_name}'")
