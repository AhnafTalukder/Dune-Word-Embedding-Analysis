import os
from dotenv import load_dotenv

from openai import OpenAI

from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

#ACCESS FROM THE ENV FILE
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASTRA_DB_APPLICATION_TOKEN  = os.getenv('ASTRAPY_TOKEN')
ASTRA_DB_API_ENDPOINT = os.getenv('ASTRA_DB_API_ENDPOINT')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')

embedding = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=OPENAI_API_KEY)

vstore = AstraDBVectorStore(
    embedding=embedding,
    namespace=ASTRA_DB_KEYSPACE,
    collection_name="DuneEmbeddings",
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
)


def create_embeddings():

  #Read the body of text and store it in content
  file = open("./data/Dune.txt", "r")
  content = file.read()
  file.close()

  # Transform into LangChain "Documents"
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
  all_splits = text_splitter.split_text(content)

  docs = [Document(page_content=chunk) for chunk in all_splits]

  # Compute vector embedding and store entries
  inserted_ids = vstore.add_documents(docs)
  print(f"\nInserted {len(inserted_ids)} documents.")

def similarity_search(query):
  results = vstore.similarity_search(query, k=3)
  print(f"* {results[0].page_content} [{results[0].metadata}]")


#create_embeddings()
similarity_search("A poem about fear.")


