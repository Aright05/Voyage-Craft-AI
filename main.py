from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever
from generator import Generator

app = FastAPI()
retriever = Retriever()
generator = Generator()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "RAG FastAPI is live! use /docs to test the API."}

@app.post("/rag/")
def rag_response(request: QueryRequest):
    print("🔍 Received query:", request.query)
    context_passages = retriever.retrieve(request.query)
    
    if not context_passages:
        return {"error": "No relevant context found.","query": request.query}
    
    context = "\n".join(context_passages)
    print("💦combined context:\n", context)

    answer = generator.generate(request.query,context)
    print("🔥 Generated answer:", answer)

    return {
        "answer": answer,
        "context_used": context_passages
    }