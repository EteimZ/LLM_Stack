import pinecone
import os

# Connect to Pinecone
pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment=os.environ["PINECONE_ENVIRONMENT"])

# Get the quickstart index
index = pinecone.Index("quickstart")

# Query the index to get the top 3 similar vectors
query = index.query(
  vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
  top_k=3,
  include_values=True
)

# print the result
print(query)
