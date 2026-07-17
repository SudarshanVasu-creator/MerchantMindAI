from openai import OpenAI

from app.config import settings


client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url=settings.GROQ_BASE_URL,
)

models = client.models.list()

print("\n" + "=" * 60)
print("Available Groq Models")
print("=" * 60)

for model in models.data:
    print(model.id)