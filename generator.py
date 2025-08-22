import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class Generator:
    def __init__(self):
        # Configure Gemini API
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        # Choose a model (you can use "gemini-1.5-flash" or "gemini-1.5-pro")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate(self, query, context):
        prompt = f"""Use the following context to answer the question:
Context:
{context}

Question:
{query}

Answer:"""

        response = self.model.generate_content(prompt)
        return response.text
