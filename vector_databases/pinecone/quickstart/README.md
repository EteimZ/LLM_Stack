# PineCone Quickstart

This is a quick introduction to the vector database known as [Pinecone](https://www.pinecone.io/).

## Usage

Install the pinecone client:

```bash
pip install pinecone-client
```

Create a pinecone account and get your api key and environment from their console.
Set these as environemt variables:

```bash
export PINECONE_API_KEY=XXXX-YYYY-ZZZZ
export PINECONE_ENVIRONMENT=us-west1-XXX-ZZZ 
```

## Files

This example contains three files that interact with pinecone DB:

- `index.py`: This file is used to create a new index in the pinecone database.
- `retrieval.py`: This file is used to query the vector database.
- `delete.py`: This is used to delete the created index.
