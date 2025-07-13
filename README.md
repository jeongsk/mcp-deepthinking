# mcp-deepthinking

An MCP (Model Context Protocol) server that provides a **deep thinking** tool powered by Large Language Models. This server enables complex reasoning, multi-step problem solving, and advanced planning capabilities through a simple API interface.

---

## Features

- **Deep Thinking Tool**: Exposes a tool named `deepthinking` for complex reasoning tasks
- **Multiple LLM Providers**: Supports Groq, OpenAI, Anthropic, and other providers
- **Configurable Models**: Supports multiple models from different providers
- **Async & Streaming Support**: Designed for efficient, asynchronous operation
- **Easy Integration**: Compatible with any MCP client

---

## Requirements

- **Python** >= 3.12
- **API Key** from one of the supported providers:
  - Groq API Key (sign up at [https://console.groq.com/](https://console.groq.com/))
  - OpenAI API Key
  - Anthropic API Key
  - Or other supported providers

---

## Getting Started

### 1. Installation

Clone the repository and install dependencies using `uv` (recommended):

```bash
git clone <repository-url>
cd mcp-deepthinking
uv install
```

Alternatively, you can use pip:

```bash
pip install -e .
```

### 2. Configuration

Create a `.env` file in the project root with your provider configuration:

**For Groq:**
```env
PROVIDER=groq
API_KEY=your_groq_api_key_here
MODEL_ID=deepseek-r1-distill-llama-70b
```

**For OpenAI:**
```env
PROVIDER=openai
API_KEY=your_openai_api_key_here
MODEL_ID=gpt-4o
```

**For Anthropic:**
```env
PROVIDER=anthropic
API_KEY=your_anthropic_api_key_here
MODEL_ID=claude-3-5-sonnet-20241022
```

**Configuration Options:**
- `PROVIDER` (required): The LLM provider (`groq`, `openai`, `anthropic`, etc.)
- `API_KEY` (required): Your API key for the chosen provider
- `MODEL_ID` (optional): Specific model to use (defaults to provider's recommended model)

### 3. Running the Server

Start the MCP server:

```bash
uv run mcp_deepthinking
```

This will start the server using **stdio** transport, ready to accept MCP client connections.

---

## Usage

### From MCP Client

From an MCP-compatible client, you can invoke the `deepthinking` tool with a query string:

```python
response = mcp.call_tool("deepthinking", {
    "query": "Explain the theory of relativity step by step."
})
print(response)
```

### Example Query

```python
query = """
I need to plan a complex software architecture for a distributed system 
that handles real-time data processing. What are the key considerations 
and design patterns I should implement?
"""

response = mcp.call_tool("deepthinking", {"query": query})
```

The tool will return a detailed reasoning response with step-by-step analysis and recommendations.

---

## Tool Details

### `deepthinking(query: str) -> str`

A tool that performs deep reasoning and analysis for complex problems. It can be used for:

- Complex problem solving
- Multi-step planning and analysis
- Technical architecture decisions
- Strategic thinking and planning
- Academic research and analysis

**Arguments:**
- `query` (str): The input prompt, question, or problem to analyze

**Returns:**
- `str`: A comprehensive reasoning response with detailed analysis and conclusions

---

## Supported Models

### Groq Models
- `deepseek-r1-distill-llama-70b` (default)
- `deepseek-r1-distill-qwen-32b`
- `qwen-qwq-32b`

### OpenAI Models
- `gpt-4o` (default)
- `gpt-4o-mini`
- `o1-preview`
- `o1-mini`

### Anthropic Models
- `claude-3-5-sonnet-20241022` (default)
- `claude-3-5-haiku-20241022`
- `claude-3-opus-20240229`

---

## Development

### Project Structure

```
mcp-deepthinking/
├── src/
│   └── mcp_deepthinking/
│       ├── __init__.py
│       ├── __main__.py
│       ├── server.py
│       └── settings.py
├── pyproject.toml
├── .env
└── README.md
```

### Running in Development Mode

```bash
# Install in development mode
uv install --dev

# Run with debug logging
DEBUG=1 uv run mcp_deepthinking
```

---

## License

MIT License

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Contact

For questions or support, please open an issue on the project repository.
