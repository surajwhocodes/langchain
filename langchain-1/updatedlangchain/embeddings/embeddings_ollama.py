import os
from langchain_ollama import OllamaEmbeddings

llm = OllamaEmbeddings(model="llama3.2")

text = input("Enter the Text")
response = llm.embed_query(text)
print(response)