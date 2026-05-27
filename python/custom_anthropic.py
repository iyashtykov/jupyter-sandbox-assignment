import os
import requests

anthropic_custom_url = os.environ.get("ANTHROPIC_CUSTOM_URL", "")
anthropic_custom_key = os.environ.get("ANTHROPIC_CUSTOM_KEY", "")

sub_path = "/v1/messages"
llm_url = f"{anthropic_custom_url.rstrip('/')}{sub_path}"
llm_model = "claude-sonnet-4-5"

headers = {
    "x-api-key": anthropic_custom_key,
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01"
}

payload = {
    "max_tokens": 500,
    "model": llm_model,
    "messages": [
        {
            "role": "user",
            "content": "great indent in python"
        }
    ]
}

try:
    response = requests.post(llm_url, headers=headers, json=payload)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")