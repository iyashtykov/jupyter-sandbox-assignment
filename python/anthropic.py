import os
import requests
import json
import sys

# 1. Environment & Variable Setup
# Using .get() to avoid KeyErrors if variables are missing
api_key = os.getenv("ANTHROPIC_API_KEY")
base_url = os.getenv("ANTHROPIC_BASE_URL")
model_name = "claude-sonnet-4-5"

print("--- INITIALIZATION DEBUG ---")
print(f"DEBUG: Base URL: {base_url}")
print(f"DEBUG: API Key Loaded: {'Yes' if api_key else 'No'}")

if not api_key or not base_url:
    print("ERROR: Missing environment variables. Please check ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL.")
    # If variables are missing, the script stops here
    sys.exit(1)

# 2. URL and Header Construction
# Ensures no double slashes in the final URL
url = f"{base_url.rstrip('/')}/v1/messages"

headers = {
    "Authorization": f"Bearer {api_key}",
    "anthropic-version": "2023-06-01",
    "Content-Type": "application/json"
}

payload = {
    "model": model_name,
    "max_tokens": 500,
    "messages": [
        {"role": "user", "content": "python indent examples"}
    ]
}

print(f"DEBUG: Sending request to {url}...")

# 3. Execution and Response Parsing
try:
    # Timeout set to 30s to prevent Jupyter from hanging indefinitely
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    
    print(f"DEBUG: HTTP Status Code: {response.status_code}")

    if response.status_code == 200:
        # Success: Extracting the text from Anthropic's specific JSON structure
        result = response.json()
        
        # Anthropic response path: content -> list -> first item -> text
        if 'content' in result and len(result['content']) > 0:
            ai_text = result['content'][0].get('text', 'No text in response content.')
            print("\n" + "="*20 + " AI RESPONSE " + "="*20)
            print(ai_text)
            print("="*53)
        else:
            print("DEBUG: Response received but 'content' field is missing or empty.")
            print(json.dumps(result, indent=2))
            
    else:
        # Error: Printing the raw error message from the server
        print("\n--- API ERROR RESPONSE ---")
        print(f"Status: {response.status_code}")
        print(f"Raw Body: {response.text}")

except requests.exceptions.Timeout:
    print("ERROR: The request timed out. The server took too long to respond.")
except requests.exceptions.ConnectionError:
    print("ERROR: Connection failed. Check if the BASE_URL is correct and reachable from this container.")
except Exception as e:
    print(f"ERROR: An unexpected error occurred: {type(e).__name__}: {e}")