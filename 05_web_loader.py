
from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apnacollege.in/course/sigma-9"

loader = WebBaseLoader(web_paths=(url,))
documents = loader.load()

print("Total documents:", len(documents))
print(documents[0].page_content[:1000])
print(documents[0].metadata)
