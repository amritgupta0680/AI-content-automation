from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from utils import load_knowledge_base

class RAGSystem:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []
        self._load_knowledge_base()
    
    def _load_knowledge_base(self):
        """Load and index knowledge base"""
        self.documents = load_knowledge_base()
        if self.documents:
            embeddings = self.model.encode(self.documents)
            dimension = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
            self.index.add(np.array(embeddings).astype('float32'))
    
    def add_document(self, text):
        """Add new document to knowledge base"""
        embedding = self.model.encode([text])
        if self.index is None:
            dimension = embedding.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
        
        self.index.add(np.array(embedding).astype('float32'))
        self.documents.append(text)
        from utils import save_to_knowledge_base
        save_to_knowledge_base(text)
    
    def retrieve(self, query, k=3):
        """Retrieve relevant documents"""
        if not self.documents or self.index is None:
            return ""
        
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(query_embedding).astype('float32'), k
        )
        
        context = ""
        for idx in indices[0]:
            if idx < len(self.documents):
                context += self.documents[idx] + "\n\n"
        
        return context[:2000]

# Global instance
rag = RAGSystem()