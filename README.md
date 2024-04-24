## AutoCortext API CLient

This is a cimple client for the AutoCortext API.

### Setup

1. A `.env` file with the variable `AUTOCORTEXT_API_KEY` set to a valid key.
2. An organization ID

### Example

```python
import autocortext
import json

msg = '[{ "id":1, "content":"How can I help you?" ,"role":"assistant"}, { "id":2, "content":"Why is the sky blue?","role":"user"}]'

client = autocortext.AutoCortext(organization_id="12345")
res = client.troubleshoot(msg)

msgs = json.loads(res)
for msg in msgs:
    if msg["id"] == 3 and msg["role"] == "assistant":
        print(msg["content"])
```
