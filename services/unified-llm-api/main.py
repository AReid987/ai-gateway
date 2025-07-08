from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import litellm
import os

app = FastAPI()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
    provider = body.get('provider', 'openai')
    model = body.get('model', 'gpt-3.5-turbo')
    messages = body.get('messages', [])
    try:
        response = litellm.completion(
            model=model,
            messages=messages,
            api_base=None,
            api_key=None,
        )
        return JSONResponse(response)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

