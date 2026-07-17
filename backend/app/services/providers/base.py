from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base interface for all LLM providers.
    """

    @abstractmethod
    def invoke(self, prompt: str) -> str:
        """
        Send a prompt to the provider and return its response.
        """
        pass