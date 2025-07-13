import asyncio
import os

from mcp_deepthinking.server import serve


def main():
    """MCP Deepthinking main entry point."""

    # groq, deepseek, ollama
    provider = os.getenv("PROVIDER", "groq")
    if provider not in ["groq", "deepseek", "ollama"]:
        raise ValueError(
            f"Unsupported MCP provider: {provider}. Supported providers are 'groq', 'deepseek', and 'ollama'."
        )

    api_key = os.getenv("API_KEY", "")
    model_id = os.getenv("MODEL_ID", "")

    if provider == "groq":
        api_key = os.getenv("GROQ_API_KEY", api_key)
        if api_key is None:
            raise ValueError("GROQ_API_KEY environment variable is not set.")
        model_id = os.getenv("MODEL_ID", "deepseek-r1-distill-llama-70b")
    elif provider == "deepseek":
        api_key = os.getenv("DEEPSEEK_API_KEY", api_key)
        if api_key is None:
            raise ValueError("DEEPSEEK_API_KEY environment variable is not set.")
        model_id = os.getenv("MODEL_ID", "deepseek-reasoner")
    elif provider == "ollama":
        model_id = os.getenv("MODEL_ID", "deepseek-r1")

    asyncio.run(serve(api_key, provider, model_id))


if __name__ == "__main__":
    main()
