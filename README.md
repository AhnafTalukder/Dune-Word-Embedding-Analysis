<a name="readme-top"></a>

<h3 align="center">Word Embeddings Analysis and Semantic Search Optimization with Dune</h3>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="assets/Dune.jpg" alt="Logo">
  
  <p align="center">
   "Deep in the human unconscious is a pervasive need for a logical universe that makes sense. But the real universe is always one step beyond logic." - from "The Sayings of Muad'Dib"
    <br />
    <a href="/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="/">View Demo</a>
    ·
    <a href="/">Report Bug</a>
    ·
    <a href="/">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

My goal with this project was to leverage OpenAI’s embedding model to analyze text from  the "Dune" book series by Frank Herbert. More specifically, I wanted to understand how words, characters, and motifs are grouped together. I sought to do this using OpenAI’s pretrained model and open-source tools like LangChain, which abstracts the complex logic of deep learning.

Applications:
* **Semantic Search**: Do searches based on semantics (meaning) rather than syntax, using Euclidean or cosine similarity search. This can allow people to go through a book based on descriptions they recall rather than a page number, simplifying the reading of large digital documents, PDFs, and Kindle books.
* **Visualization**: PCA can be done to decrease the dimensionality of each vector, allowing words and phrases to be visualized in graphs. This enables academics and researchers to understand relationships between words and concepts in a text.
* **Chatbot Training**: The vector database can act as a brain for pre-trained Language Models. For instance, you can train ChatGPT using embeddings from "Dune" and have it role-play as Paul Atreides, the main character.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project is built using:
* [LangChain](https://github.com/hwchase17/langchain)
* [OpenAI](https://beta.openai.com/)
* [AstraDB](https://www.datastax.com/products/datastax-astra)
* [Python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username/Dune-Word-Embedding-Analysis.git
2. Install required Python packages
   ```sh
    pip install -r requirements.txt

3. Create a .env file in the project root and add your API keys
   ```env
    OPENAI_API_KEY=your_openai_api_key
    ASTRAPY_TOKEN=your_astradb_application_token
    ASTRA_DB_API_ENDPOINT=your_astradb_api_endpoint
    ASTRA_DB_KEYSPACE=your_astradb_keyspace
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- USAGE EXAMPLES -->

### Usage

1. Create Embeddings
    ```python
    create_embeddings('path_to_your_text_file.txt')
    
2. Tokenize Text
    ```python
    tokenize_text('path_to_your_text_file.txt')
3. Ask Questions
    ```python
    ask_question("DuneEmbeddings")

<p align="right">(<a href="#readme-top">back to top</a>)</p>
