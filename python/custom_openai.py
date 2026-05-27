import os
import requests

openai_custom_url = os.environ.get("OPENAI_CUSTOM_URL", "")
openai_custom_key = os.environ.get("OPENAI_CUSTOM_KEY", "")

sub_path = "/v1/chat/completions"
llm_url = f"{openai_custom_url.rstrip('/')}{sub_path}"
llm_model = "gpt-4o"

headers = {
    "Authorization": f"Bearer {openai_custom_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": llm_model,
    "messages": [
        {
            "role": "system",
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