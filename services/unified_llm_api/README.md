# Unified LLM API Service

This service provides a unified OpenAI-compatible API for multiple LLM providers (Gemini, OpenRouter, Mistral, Groq, Cerebras, Chutes, VoidAI, and more).

## Usage

### Authentication
All requests must include an API key in the `apikey` header. See the main project README for details.

### Example Request (default Gemini)
```
curl -X POST http://localhost:8000/llm/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "apikey: test-api-key-123" \
  -d {model: gemini-pro, messages: [{role: user, content: Hello!}]}
```

### Example Request (specifying provider)
```
curl -X POST http://localhost:8000/llm/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "apikey: test-api-key-123" \
  -d {model: mistral-tiny, messages: [{role: user, content: Hi!}], provider: mistral}
```

## Supported Providers
- gemini (default)
- openai
- openrouter
- mistral
- groq
- cerebras
- chutes
- voidai
- huggingface
- cloudflare (stub)
- github (stub)

## Environment Variables
See `.env.example` for required API keys.


## Running Tests

To run tests locally:
```bash
pdm install
pdm run pytest -v
```

