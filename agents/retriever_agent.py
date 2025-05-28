# indexes and retrieves text

import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
text_store = []

def index_data(chunks):
    vectors = model.encode(chunks)
    index.add(np.array(vectors))
    text_store.extend(chunks)

def retrieve_top_k(query, k=3):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), k)
    return [text_store[i] for i in I[0]]
