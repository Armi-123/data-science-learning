from langchain.chains import RetrievalQA
from langchain_community.llms import GPT4All
from vector_store import build_vector_store

def create_chatbot():
    # Build vector store
    vector_store = build_vector_store()

    # Load local GPT4All model
    llm = GPT4All(
        model="ggml-gpt4all-j-v1.3-groovy.bin",
        model_path="models/",
        n_ctx=512,
        temperature=0.2,
        allow_download=True
    )

    # RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever()
    )

    return qa_chain
