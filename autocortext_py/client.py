import os
import requests
import json


class AutoCortext:
    def __init__(self):
        self.base_url = "https://ascend-six.vercel.app/"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('AUTOCORTEXT_API_KEY')}",
        }

    def troubleshoot(self, message):
        response = requests.post(
            f"{self.base_url}/api/read?companyId={os.getenv('AUTOCORTEXT_ORG_ID')}",
            headers=self.headers,
            data=message,
        )
        return response.text
