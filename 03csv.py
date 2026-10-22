
from pathlib import Path
from langchain_community.document_loaders import CSVLoader

file_path = Path(__file__).parent / "students.csv"

loader = CSVLoader(file_path=str(file_path))
documents = loader.load()

print("Total documents:", len(documents))

print("\n--- Row 1 ---")
print(documents[0].page_content)
print("Metadata:", documents[0].metadata)

print("\n--- Row 2 ---")
print(documents[1].page_content)
print("Metadata:", documents[1].metadata)

print("\n--- Row 3 ---")
print(documents[2].page_content)
print("Metadata:", documents[2].metadata)
