import asyncio
import os

from .server import serve


def main():
    """MCP Deepthinking main entry point."""

    api_key = os.getenv("GROQ_API_KEY")
    if api_key is None:
        raise ValueError("GROQ_API_KEY environment variable is not set.")
    
    model_id = os.getenv("MODEL_ID", "deepseek-r1-distill-llama-70b")

    asyncio.run(serve(api_key, model_id))

__all__ = ["main", "server", "__version__"]

if __name__ == "__main__":
    main()
