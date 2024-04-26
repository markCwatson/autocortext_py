## Simple AutoCortext API Client

This is a simple client for the AutoCortext API.

### Setup

1. An `.env` file with the variable `AUTOCORTEXT_API_KEY` set to a valid key.
1. An `.env` file with the variable `AUTOCORTEXT_ORG_ID` set to a valid organization ID.

### Example

Install the AutoCortext clinet using `pip`.

```shell
pip install autocortext-py
```

Use the client in your source code.

```python
import os
from autocortext_py import AutoCortext
from dotenv import load_dotenv

load_dotenv()

client = AutoCortext(
    org_id=os.getenv("AUTOCORTEXT_ORG_ID"),
    api_key=os.getenv("AUTOCORTEXT_API_KEY"),
)

client.config(verbosity="concise", machine="Conveyor System", system="Electrical")

res = client.troubleshoot("The 24 volt system in the conveyor is not powering on.")
print(res)

client.set_verbosity("verbose")
res = client.troubleshoot("OK how do I fix it?")
print(res)

client.save()
```
