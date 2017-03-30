"""TwitterKeys loads Twitter API keys from a JSON file."""
import json

def getKeys():
    """Retrieve a tuple of API keys for the application."""
    data = json.load(open("keys.json"))
    return (data["ACCESS_TOKEN"], data["ACCESS_TOKEN_SECRET"],
            data["CONSUMER_KEY"], data["CONSUMER_KEY_SECRET"])
