from langchain_community.vectorstores import FAISS
from backend.embeddings import embedding_model


def load_vector_store():

    vector_db = FAISS.load_local(
        "vectorstore",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_db


def retrieve_documents(query):

    vector_db = load_vector_store()

    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 15
        }
    )

    return retriever.invoke(query)