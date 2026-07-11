from backend.rag import ask_health_advisor

question = input("Ask your question: ")

answer = ask_health_advisor(question)

print("\n")
print("=" * 70)
print(answer)