from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

def build_vector_store():
    # Read store data
    with open("d:/Unlox/Week_5/ecommerce_chatbot/src/data/store_data.txt", "r", encoding="utf-8") as f:
        data = f.read()

    # Split text into chunks
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0)
    docs = splitter.split_text(data)

    # Embedding model
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Build FAISS vector store
    vector_store = FAISS.from_texts(texts=docs, embedding=embeddings)

    return vector_store
