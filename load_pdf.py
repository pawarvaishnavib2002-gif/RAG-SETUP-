# from langchain_communit
# y.document_loadyPDFLoader

from langchain_community.document_loaders import PyPDFLoader

# Load your PDF file
loader = PyPDFLoader("AI_Data_Science_Interview_QA.pdf")

# Read the PDF
documents = loader.load()

# Print the total pages
print("Total pages:", len(documents))

# Print the first page text
print(documents[0].page_content)
