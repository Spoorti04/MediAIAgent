from backend.retriever import retrieve_documents

query = input("Question: ")

docs = retrieve_documents(query)

for i, doc in enumerate(docs, 1):
    print("\n", "="*60)
    print(f"Document {i}")
    print("="*60)
    print(doc.page_content)