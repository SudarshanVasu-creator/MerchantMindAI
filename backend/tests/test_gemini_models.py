from google import genai

from app.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

print("=" * 60)
print("Available Gemini Models")
print("=" * 60)

for model in client.models.list():
    print(f"\n{model.name}")

    if hasattr(model, "display_name"):
        print(f"Display Name : {model.display_name}")

    if hasattr(model, "description"):
        print(f"Description  : {model.description}")