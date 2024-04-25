import requests
import json


class AutoCortext:
    def __init__(self, org_id, api_key):
        if not org_id:
            raise ValueError("Organization ID must be provided and cannot be empty.")
        if not api_key:
            raise ValueError("API key must be provided and cannot be empty.")

        self.base_url = "https://ascend-six.vercel.app/"
        self.org_id = org_id
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def troubleshoot(self, message):
        # Convert message to a Python dict if it's not already one
        if isinstance(message, str):
            try:
                message = json.loads(message)
            except json.JSONDecodeError:
                raise ValueError("Message must be a valid JSON string or a dictionary.")

        # Ensure message is a list of dicts
        if isinstance(message, list) and all(isinstance(m, dict) for m in message):
            # Find the highest current ID and add 1
            max_id = max(msg["id"] for msg in message) if message else 0
            message.append(
                {
                    "id": max_id + 1,
                    "content": "Also, please keep your response as short as possible.",
                    "role": "user",
                }
            )
        else:
            raise ValueError(
                "Message must be a list of dictionaries with at least an 'id' key."
            )

        # Convert the list of messages into a single context string
        context = "\n".join(msg["content"] for msg in message)

        response = requests.post(
            f"{self.base_url}/api/read?companyId={self.org_id}",
            headers=self.headers,
            json=context,
        )

        if response.status_code == 200:
            try:
                response_data = response.json()
                return response_data.get("data", "No data found")
            except json.JSONDecodeError:
                return "Invalid JSON response"
        else:
            return f"Error: {response.status_code} - {response.text}"
