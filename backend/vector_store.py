from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):
    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    vector_db.save_local("vectorstore")

    return vector_db