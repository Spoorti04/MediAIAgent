from backend.loader import load_documents
from backend.splitter import split_documents
from backend.embeddings import embedding_model
from backend.vector_store import create_vector_store

print("=" * 60)
print("Loading Medical Documents...")
print("=" * 60)

documents = load_documents()

print(f"Loaded {len(documents)} pages.")

print("\nSplitting Documents...")

chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks.")

print("\nCreating FAISS Vector Database...")

create_vector_store(chunks, embedding_model)

print("\nVector Database Created Successfully!")
print("Saved in vectorstore/")