import os
import requests
import json
import sys

# 1. Configuration & Environment Check
# Ensure these variables are set in your environment or defined here
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

# Basic debug info to see if variables are actually loaded
print(f"DEBUG: Base URL is set to: {base_url}")
print(f"DEBUG: API Key exists: {'Yes' if api_key else 'No'}")

if not api_key or not base_url:
    print("ERROR: Environment variables OPENAI_API_KEY or OPENAI_BASE_URL are missing.")
    # Uncomment the line below to see all available env vars if needed
    # print(os.environ.keys())
    sys.exit(1)

# 2. URL Formatting
# Clean up trailing slashes to avoid '//chat/completions'
clean_url = f"{base_url.rstrip('/')}/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "user", "content": "Explain python loops"}
    ]
}

print(f"DEBUG: Sending POST request to: {clean_url}...")

# 3. Execution with Exception Handling
try:
    # Added a 30-second timeout to prevent the script from hanging indefinitely
    response = requests.post(clean_url, headers=headers, json=payload, timeout=30)
    
    # Print HTTP Status Code (200 is Success)
    print(f"DEBUG: HTTP Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        # Extracting the actual message content
        content = data['choices'][0]['message']['content']
        print("\n--- AI RESPONSE ---")
        print(content)
    else:
        # If the API returns an error (e.g., 401, 404, 500)
        print("\n--- API ERROR ---")
        print(f"Status: {response.status_code}")
        print(f"Details: {response.text}")

except requests.exceptions.Timeout:
    print("ERROR: The request timed out. Check your network or Proxy settings.")
except requests.exceptions.ConnectionError:
    print("ERROR: Could not connect to the server. Check your BASE_URL.")
except Exception as e:
    print(f"ERROR: An unexpected error occurred: {type(e).__name__}")
    print(str(e))