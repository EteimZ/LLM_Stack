import json

from client import client

while (query := input("Input Query: ")) != "exit":

    nearText = {"concepts": [query]}

    response = (
        client.query
        .get("QuotesByBook", ["author", "quote"])
        .with_near_text(nearText)
        .with_limit(2)
        .do()
    )

    print(json.dumps(response, indent=2))
