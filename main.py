import os
from dotenv import load_dotenv

from langchain_openai import OpenAI
from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.indexes.vectorstore import VectorStoreIndexWrapper


load_dotenv()

#ACCESS FROM THE ENV FILE
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASTRA_DB_APPLICATION_TOKEN  = os.getenv('ASTRAPY_TOKEN')
ASTRA_DB_API_ENDPOINT = os.getenv('ASTRA_DB_API_ENDPOINT')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')

embedding = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=OPENAI_API_KEY)


# Create text embeddings
def create_embeddings(file_name):

  vstore = AstraDBVectorStore(
    embedding=embedding,
    namespace=ASTRA_DB_KEYSPACE,
    collection_name="DuneEmbeddings",
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
  )


  #Read the body of text and store it in content
  file = open(file_name, "r")
  content = file.read()
  file.close()

  # Transform into LangChain "Documents"
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
  all_splits = text_splitter.split_text(content)

  docs = [Document(page_content=chunk) for chunk in all_splits]

  # Compute vector embedding and store entries
  inserted_ids = vstore.add_documents(docs)
  print(f"\nInserted {len(inserted_ids)} documents.")

# Create embeddings for words
def tokenize_text(file_name):

  vstore = AstraDBVectorStore(
    embedding=embedding,
    namespace=ASTRA_DB_KEYSPACE,
    collection_name="DuneTokens",
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
  )

  file = open(file_name, "r")
  content = file.read()
  file.close()
  tokens = content.split()

  docs = [Document(page_content=token) for token in tokens]

  # Compute vector embedding and store entries
  inserted_ids = vstore.add_documents(docs)
  print(f"\nInserted {len(inserted_ids)} documents.")


def similarity_search(query, collection_str):

  print("Starting similarity search")

  vstore = AstraDBVectorStore(
    embedding=embedding,
    namespace=ASTRA_DB_KEYSPACE,
    collection_name=collection_str,
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
  )

  try:
    results = vstore.similarity_search_with_score(query, k=4)
    print("similarity search complete")
    return results
  except:
    print("similarity search failed.")
    return None

  


def ask_question(collection_str):

  #accessing the vstore for a specific collection
  vstore = AstraDBVectorStore(
    embedding=embedding,
    namespace=ASTRA_DB_KEYSPACE,
    collection_name=collection_str,
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
  )

  #prompt the user
  while True:

    vectorIndex = VectorStoreIndexWrapper(vectorstore=vstore)
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    print("(Type \"quit\" to end)")
    question = input("Ask me any question about Dune Book 1 and 2: ")

    if(question.lower() == "quit"):
      print("I wish you well on your Dune journey.")
      break
    
    #query the database for answer
    print("QUESTION: \"%s\"" % question)
    print("Analyzing question....\n")
    answer = vectorIndex.query(question, llm=llm).strip()
    print("ANSWER: \"%s\" \n" % answer)

    print("PARAGRAPHS OF RELEVANCE:")
    relevant_paragraphs = similarity_search(question, collection_str)
    for paragraph, score in relevant_paragraphs:
      print( " %0.4f \"%s ...\"" % (score, paragraph.page_content[:60]))

 
      
ask_question("DuneEmbeddings")




