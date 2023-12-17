import weaviate

# Connect to the weaviate database
client = weaviate.Client(
    url = "http://localhost:8080",
    additional_headers={
        "X-OpenAI-Api-Key": "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",
    }
)
