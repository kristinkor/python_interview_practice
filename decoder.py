import base64

# The Base64 encoded content inside the JSON array
encoded_content = "SnVwaXRlciBpcyB0aGUgbW9zdCBtYXNzaXZlIHBsYW5ldCBpbiBvdXIgU29sYXIgU3lzdGVtLCBtZWFuaW5nIGl0IGFsc28gaGFzIHRoZSBoaWdodGVzdCBncml2aXR5LiBJZiB5b3Ugc3RvbmQgb24gSnVwaXRlciDigJMgeW91IGNhbm5vdCBiZWNhdXNlIGl0IGRvZXMgbm90IGhhdmUgYSBzb2xpZCBzdXJ"

# Decode the Base64 string
decoded_content = base64.b64decode(encoded_content).decode("utf-8")

# Print the decoded content
print(decoded_content)