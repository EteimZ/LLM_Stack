import csv
from client import client

# Define a class
class_obj = {
  "class": "QuotesByBook",
  "vectorizer": "text2vec-openai",
  "moduleConfig": {
    "text2vec-openai": {
      "model": "ada",
      "modelVersion": "002",
      "type": "text"
    }
  }
}

# create the class
client.schema.create_class(class_obj)

# Load data
csv_file_path = "data/quotesbybook.csv"

csv_file = open(csv_file_path, 'r')
quotes_data = csv.reader(csv_file)

# Import data into weaviate
with client.batch(
    batch_size=100
) as batch:
    # Batch import all Questions
    for quote in quotes_data:

        properties = {
            "Author": quote[0],
            "Quote": quote[1],
        }

        client.batch.add_data_object(
            properties,
            "QuotesByBook",
        )

print("Successfully uploaded data to weaviate!")
csv_file.close()