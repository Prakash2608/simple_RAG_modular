from langchain_community.document_loaders import WebBaseLoader
import bs4
from src.logger.logging import logging
from src.exceptions.exception import customexception
import sys



class DocumentLoaderConfig:
    web_path:str = "https://lilianweng.github.io/posts/2023-06-23-agent/"


class DocumentLoader:
    def __init__(self): 
        self.web_path = DocumentLoaderConfig
        
    def initiate_document_loader(self):
        logging.info("Document loader initiated.")
        try:
            loader = WebBaseLoader(
                web_paths = (self.web_path,),
                bs_kwargs=dict(
                    parse_only=bs4.SoupStrainer(
                        class_=("post-content", "post-title", "post-header")
                    )
                )
            )
            docs = loader.load()
            return docs
        except Exception as e:
            logging.info("Exception occured in document loader part")
            raise customexception(e, sys)
        
        

# Load Documents
# loader = WebBaseLoader(
#     web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
#     bs_kwargs=dict(
#         parse_only=bs4.SoupStrainer(
#             class_=("post-content", "post-title", "post-header")
#         )
#     ),
# )
# docs = loader.load()