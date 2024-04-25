import requests
import json


class AutoCortext:
    """
    A client for interacting with the AutoCortext API.

    This class provides methods to send messages and receive responses from the AutoCortext API.

    Attributes:
        org_id (str): The organization ID required for API requests.
        api_key (str): The API key used for secure communication with the API.
        base_url (str): The base URL for the API endpoints.
    """

    def __init__(self, org_id, api_key):
        """
        Initializes the AutoCortext client with necessary authentication credentials.

        Args:
            org_id (str): The organization ID for the API.
            api_key (str): The API key for accessing the API.

        Raises:
            ValueError: If either org_id or api_key is not provided.
        """
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
        """
        Sends a troubleshooting message to the API and returns the response.

        The method expects a message in the form of a string or a dictionary and sends it
        as a JSON payload to the API's troubleshooting endpoint.

        Args:
            message (str or dict): The message or context to be sent for troubleshooting.

        Returns:
            str: The response from the API, typically containing troubleshooting information.

        Raises:
            ValueError: If the message is neither a string nor a dictionary.
            JSONDecodeError: If the response from the API is not valid JSON.
        """
        if isinstance(message, str):
            try:
                # Convert message to a Python dict if it's not already one
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
                    "content": "User: Also, please keep your response as short as possible.",
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
