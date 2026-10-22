from pathlib import Path
from langchain_community.document_loaders import JSONLoader

file_path = Path(__file__).parent / "03students.json"

loader = JSONLoader(
    file_path=str(file_path),
    jq_schema=".[]",
    text_content=False
)

documents = loader.load()

print("Total documents:", len(documents))
print(documents[0].page_content)
print(documents[1].page_content)
print(documents[2].page_content)