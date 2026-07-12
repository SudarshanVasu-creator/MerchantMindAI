from app.services.llm import LLMService


llm = LLMService()

response = llm.invoke(
    "Reply with exactly one word: SUCCESS"
)

print(response)