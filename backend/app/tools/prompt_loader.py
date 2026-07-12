from pathlib import Path

from jinja2 import Template

from app.core.logging import logger


BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROMPTS_DIR = BASE_DIR / "app" / "prompts" / "agents"


def load_prompt(prompt_name: str,  **context) -> str:
    """
    Load and render a Jinja2 prompt template.
    """

    prompt_file = PROMPTS_DIR / prompt_name

    logger.info("Loading prompt: %s", prompt_file.name)

    with prompt_file.open("r", encoding="utf-8") as file:
        template = Template(file.read())

    rendered_prompt = template.render(**context)

    logger.info("Prompt loaded successfully.")

    return rendered_prompt