from openai import (
    APIConnectionError,
    AuthenticationError,
    BadRequestError,
    OpenAI,
    RateLimitError,
)

from app.config import settings
from app.core.exceptions import (
    ProviderAuthenticationError,
    ProviderBadRequestError,
    ProviderQuotaExceededError,
    ProviderUnavailableError,
)
from app.services.providers.base import BaseProvider


class GroqProvider(BaseProvider):
    """
    xAI Grok provider.
    """

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url=settings.GROQ_BASE_URL,
        )

        self.model = settings.GROQ_MODEL

    def invoke(self, prompt: str) -> str:

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            return response.choices[0].message.content

        except RateLimitError as e:
            raise ProviderQuotaExceededError(str(e))

        except APIConnectionError as e:
            raise ProviderUnavailableError(str(e))

        except AuthenticationError as e:
            raise ProviderAuthenticationError(str(e))

        except BadRequestError as e:
            raise ProviderBadRequestError(str(e))