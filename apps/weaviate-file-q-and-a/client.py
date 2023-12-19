import weaviate
import os

# Connect to the weaviate database
client = weaviate.Client(
    url = "http://localhost:8080",
    additional_headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"],
    }
)
