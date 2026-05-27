import os
import requests

gemini_custom_url = os.environ.get("GEMINI_CUSTOM_URL", "")
gemini_custom_key = os.environ.get("GEMINI_CUSTOM_KEY", "")

sub_path = "/v1beta/models/gemini-3.5-flash:generateContent"
llm_url = f"{gemini_custom_url.rstrip('/')}{sub_path}?key={gemini_custom_key}"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "great indent in python"
                }
            ]
        }
    ]
}

try:
    response = requests.post(llm_url, headers=headers, json=payload)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")