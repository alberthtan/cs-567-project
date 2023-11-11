import os
from pathlib import Path
from llama_index import download_loader
os.environ["OPENAI_API_KEY"] = "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"
from llama_index import StorageContext, load_index_from_storage
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

SimpleCSVReader = download_loader("SimpleCSVReader")

loader = SimpleCSVReader(encoding="utf-8")
documents = loader.load_data(file=Path('docs/goggins.csv'))

print('a')
# documents = SimpleDirectoryReader('docs').load_data()
index = GPTVectorStoreIndex.from_documents(documents)
#chat_engine = index.as_chat_engine()
index.storage_context.persist()
query_engine = index.as_query_engine()
# Run queries
while True:
    user_input = input("Enter your query (or 'exit' to stop): ")
    if user_input.lower() == 'exit':
        break
    print(query_engine.query(user_input))


