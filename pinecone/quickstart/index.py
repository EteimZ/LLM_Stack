import pinecone
import os

# Connect to Pinecone
pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment=os.environ["PINECONE_ENVIRONMENT"])

# Create an index
pinecone.create_index("quickstart", dimension=8, metric="euclidean")

# Get list of indexes
index_list = pinecone.list_indexes()

# Print the index list
print(index_list)

# Get the quickstart index
index = pinecone.Index("quickstart")

print(index)

# Add five vectors to the index
index.upsert([
    ("A", [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),
    ("B", [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]),
    ("C", [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
    ("D", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]),
    ("E", [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
])

# Get the stats of the index
stats = index.describe_index_stats()

# Print the stats
print(stats)
