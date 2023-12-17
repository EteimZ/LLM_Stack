# This will utilize weaviate as the vector Database
# Fast api as the API development framework
# OpenAI embeddings for vectorization
# gpt-3.5-turbo as the LLM

## Endpoints
# Upload file endpoint
# Query file endpoint
# Get list of files uploaded endpoint

## Technologies
# FastAPI
# Weaviate

from fastapi import FastAPI

app = FastAPI()

@app.post("/upload")
def upload_file():
    return {"detail": "File upload"}

@app.get("/query/{file_name}")
def query_file(file_name: str):
    return {"detail": f"Query file: {file_name}"}

@app.get("/list")
def list_files():
    return {"detail": "Return a list of files"}

