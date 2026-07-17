from google import genai
from google.genai.errors import ClientError, ServerError

from app.config import settings
from app.core.exceptions import (
    ProviderAuthenticationError,
    ProviderBadRequestError,
    ProviderQuotaExceededError,
    ProviderUnavailableError,
)
from app.services.providers.base import BaseProvider


class GeminiProvider(BaseProvider):
    """
    Gemini API provider.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )

        self.model = settings.DEFAULT_MODEL

    def invoke(self, prompt: str) -> str:

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            return response.text

        except ServerError as e:
            raise ProviderUnavailableError(str(e))

        except ClientError as e:

            message = str(e)

            if "429" in message or "RESOURCE_EXHAUSTED" in message:
                raise ProviderQuotaExceededError(message)

            if "401" in message or "403" in message:
                raise ProviderAuthenticationError(message)

            if "400" in message:
                raise ProviderBadRequestError(message)

            raise