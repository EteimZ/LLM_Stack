import pinecone
import os

# Connect to Pinecone
pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment=os.environ["PINECONE_ENVIRONMENT"])

# Delete index
pinecone.delete_index("quickstart")

print("Successfully deleted index")
