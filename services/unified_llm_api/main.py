import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import litellm
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    start_time = datetime.now()
    body = await request.json()
    provider = body.get('provider', 'gemini')
    model = body.get('model', 'gemini-pro')

    logger.info(f"Request received | Provider: {provider} | Model: {model}")

    try:
        if provider == 'cloudflare':
            logger.warning("Cloudflare integration not implemented")
            return JSONResponse({"error": "Cloudflare Workers AI integration not yet implemented."}, status_code=501)
        elif provider == 'github':
            logger.warning("GitHub integration not implemented")
            return JSONResponse({"error": "GitHub Models API integration not yet implemented."}, status_code=501)
        else:
            response = litellm.completion(
                model=model,
                messages=body.get('messages', []),
                api_base=None,
                api_key=None,
            )
            duration = (datetime.now() - start_time).total_seconds()
            logger.info(f"Request completed | Provider: {provider} | Model: {model} | Duration: {duration:.2f}s")
            return JSONResponse(response)
    except litellm.exceptions.BadRequestError as e:
        return JSONResponse({"error": "Unsupported provider"}, status_code=501)
    except Exception as e:
        logger.error(f"Request failed | Provider: {provider} | Error: {str(e)}", exc_info=True)
        return JSONResponse({"error": str(e)}, status_code=500)
