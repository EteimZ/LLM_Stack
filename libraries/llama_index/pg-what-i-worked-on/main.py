from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load document from data folder
documents = SimpleDirectoryReader('data').load_data()

# Create an index using the documents
index = VectorStoreIndex.from_documents(documents)

# Query the index using the chat_engine
chat_engine = index.as_chat_engine()

# Enter into a REPL
chat_engine.chat_repl()

