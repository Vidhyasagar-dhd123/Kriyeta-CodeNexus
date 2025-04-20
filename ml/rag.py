from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
from langchain_core.documents import Document
import os
def rag(query):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "..", "docs", "my_knowledge.txt")
    file_path = os.path.abspath(file_path)
    loader = TextLoader(file_path,encoding='utf-8')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    embeddings = OllamaEmbeddings(model="mistral")  
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever()
    llm = ChatOllama(model="mistral",base_url=os.getenv("BASE_URL"))
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = qa_chain.run(query)
    return response

def context_retrieval(data):
    documents = [Document(page_content=data)]
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    embeddings = OllamaEmbeddings(model="mistral",base_url=os.getenv("BASE_URL"))  
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever()
    llm = ChatOllama(model="mistral")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = qa_chain.run("Extract all the context preserving all information")
    return response
