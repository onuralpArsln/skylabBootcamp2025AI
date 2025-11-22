# python3.12 -m pip install sentence-transformers
# python3.12 -m pip install scikit-learn
# python3.12 -m pip install numpy

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# --- 1) Metin yükle ---
with open("mydoc.txt", "r", encoding="utf-8") as f:
    full_text = f.read()


# --- 2) Chunk'lara böl ---
def chunk_text(text, max_len=1000):
    chunks = []
    words = text.split()

    cur = []
    count = 0
    for w in words:
        cur.append(w)
        count += len(w)
        if count > max_len:
            chunks.append(" ".join(cur))
            cur = []
            count = 0

    if cur:
        chunks.append(" ".join(cur))
    return chunks

chunks = chunk_text(full_text, max_len=1000)


# --- 3) Embedding modeli ---
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Chunk embeddingleri
chunk_embeddings = model.encode(chunks)


# --- 4) Arama Fonksiyonu ---
def search(query, top_k=3):
    query_emb = model.encode([query])
    sims = cosine_similarity(query_emb, chunk_embeddings)[0]

    # en yüksek similarity'leri seç
    top_idx = np.argsort(sims)[::-1][:top_k]

    results = []
    for idx in top_idx:
        results.append((chunks[idx], sims[idx]))

    return results


# TEST
results = search("Atlas Synchron Dataworks ne yapıyor?")
for text, score in results:
    print("SCORE:", score)
    print(text[:500], "\n")
