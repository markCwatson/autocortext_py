import os
import requests
import json


class AutoCortext:
    def __init__(self, organization_id):
        self.base_url = "https://yourapiendpoint.com"
        self.headers = {
            "Organization": organization_id,
            "Authorization": f"Bearer {os.getenv('AUTOCORTEXT_API_KEY')}",
        }

    def troubleshoot(self, message):
        response = requests.post(
            f"{self.base_url}/troubleshoot", headers=self.headers, data=message
        )
        return response.text
