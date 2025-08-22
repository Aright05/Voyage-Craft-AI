import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

class Generator :
    def init(self):
        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.3
            )
    def generate(self, query,context):
        prompt = f""" Use the following context to answer the question:
Context:
{context}

Question:
{query}

Answer:"""
        response = self.llm([HumanMessage(content=prompt)])
        return response.content