
from pathlib import Path
from langchain_community.document_loaders import CSVLoader

file_path = Path(__file__).parent / "students.csv"
documents = CSVLoader(file_path=str(file_path)).load()

print("Total documents:", len(documents))
print(documents[0].page_content, documents[1].page_content, documents[2].page_content)
