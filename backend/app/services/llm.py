import json
from urllib import response

from google import genai
from google.genai.errors import ServerError

from app.config import settings
from app.core.logging import logger


class LLMService:
    """
    Handles all communication with the LLM provider.
    """

    def __init__(self) -> None:
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )

        self.model = settings.DEFAULT_MODEL

    def invoke(self, prompt: str) -> str:
        """
        Send a prompt to the configured LLM and return its response.
        """

        logger.info("Sending request to LLM...")

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            logger.info("LLM response received.")
            return response.text
        except ServerError as e:
            logger.error("Gemini is temporarily unavailable: %s", e)
            raise Exception(
                "Gemini is temporarily overloaded. Please try again in a minute."
            )

    
    def invoke_json(self, prompt: str) -> dict:
        """
        Send a prompt to the LLM and return parsed JSON.
        """

        response = self.invoke(prompt)

        # Remove Markdown code fences if present
        response = response.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            logger.exception("Failed to parse JSON returned by Gemini.")
            raise
