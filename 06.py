
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader

folder_path = Path(__file__).parent / "documents"

loader = DirectoryLoader(
    str(folder_path),
    glob="*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)

documents = loader.load()

print("Total documents:", len(documents))
print(documents[0].page_content)
print(documents[1].page_content)
print(documents[2].page_content)
