import asyncio
import os

from .server import serve


def main():
    """MCP Deepthinking main entry point."""

    # groq, deepseek, ollama
    provider = os.getenv("MCP_PROVIDER", "groq")
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


try:
    from importlib.metadata import PackageNotFoundError, version

    __version__ = version("mcp-deepthinking")
except PackageNotFoundError:
    __version__ = "0.0.0"  # 개발용 기본 버전


__all__ = ["main", "server", "__version__"]

if __name__ == "__main__":
    main()
