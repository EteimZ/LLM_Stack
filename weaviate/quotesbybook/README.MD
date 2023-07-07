# Weaviate + QuotesByBooks

This example application shows how to upload quotes from the site [QuotesByBooks](https://quotesbybook.netlify.app/) to the Weaviate vector database. Which then enables us to perform a [semantic search](https://en.wikipedia.org/wiki/Semantic_search) on the quotes.

## Folder Structure

```bash
.
├── data
├── client.py
├── docker-compose.yml
├── main.py
├── README.MD
└── upload.py
```

- `data`: Contains the data that will be uploaded to Weaviate and the script to download the data.
- `client.py`: Contains the Weaviate client that interacts with weaviate client.
- `docker-compose.yml`: Contains the configuration for the Weaviate docker container.
- `main.py`: Contains the main script that will be executed.
- `upload.py`: Contains the script that uploads the data to Weaviate.

## Usage

Install the weaviate client:

```bash
pip install weaviate-client
```

Set openai api key:

```bash
export OPENAI_API_KEY=<your-openai-api-key>
```

Start the weaviate docker container:

```bash
docker-compose up -d
```

Upload the data to weaviate:

```bash
python upload.py
```

Run the main script:

```bash
python main.py
```

Running the will take you into a REPL where you can search for quotes. For example:

```bash
Input Query: decision making
```

The application will respond with:

```json
{
  "data": {
    "Get": {
      "QuotesByBook": [
        {
          "author": "lewis christ",
          "quote": "Whenever you feel pressured just because others are doing it, pause for a while. Give it time to notice ann wait until there is evidence to prove that it's the right action before you give in."
        },
        {
          "author": "morgan housel",
          "quote": "Intelligence is not a reliable advantage in a world that's become as connected as ours has. But flexibility is."
        }
      ]
    }
  }
}
```

Type `exit` to exit the REPL.

