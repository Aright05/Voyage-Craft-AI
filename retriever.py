from sentence_transformers import SentenceTransformer
import faiss 
class Retriever:
    def _init_(self):
        self.model= SentenceTransformer('all-MiniLM-L6-v2')
        self.texts= self.load_texts()
        
        self.embeddings= self.model.encode(self.texts,convert_to_tensor=False)
        self.index= faiss.IndexFlatL2(self.embeddings[0].shape[0])
        self.index.add(self.embeddings)
    def load_texts(self):
        with open("data/knowleadge.txt","r",encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    def retrieve(self,query,top_k=3):
        query_emb= self.model.encode([query],convert_to_tensor=False)
        distance,indices= self.index.search(query_emb,top_k)
        return [self.texts[i] for i in indices[0]]