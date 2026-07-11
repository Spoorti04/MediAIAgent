import os

from langchain_community.document_loaders import PyPDFLoader


def load_documents(data_folder="data"):

    documents = []

    for root, dirs, files in os.walk(data_folder):

        for file in files:

            if file.endswith(".pdf"):

                path = os.path.join(root, file)

                loader = PyPDFLoader(path)

                documents.extend(loader.load())

    return documents
