import pytest
from fastapi.testclient import TestClient
from unified_llm_api.main import app
from unittest.mock import patch

client = TestClient(app)

@patch('unified_llm_api.main.litellm.completion')
def test_chat_completion_success(mock_completion):
    # Create complete OpenAI-style response
    mock_completion.return_value = {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": "gemini-pro",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Hello!"
            },
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 9,
            "completion_tokens": 12,
            "total_tokens": 21
        }
    }
    
    response = client.post(
        "/v1/chat/completions",
        headers={"apikey": "test-key"},
        json={
            "model": "gemini-pro",
            "messages": [{"role": "user", "content": "Hello"}]
        }
    )
    
    assert response.status_code == 200
    response_json = response.json()
    assert "choices" in response_json
    assert len(response_json["choices"]) > 0
    assert "content" in response_json["choices"][0]["message"]


def test_unsupported_provider():
    response = client.post(
        "/v1/chat/completions",
        headers={"apikey": "test-key"},
        json={
            "model": "test-model",
            "provider": "unsupported-provider",
            "messages": [{"role": "user", "content": "Hello"}]
        }
    )
    assert response.status_code == 501
