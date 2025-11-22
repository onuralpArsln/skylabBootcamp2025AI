import gradio as gr
import os
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# .env dosyasından yükle
load_dotenv()

# API key al
api_key = os.getenv('GEMINI_API_KEY')

# Google Gemini istemcisini oluştur
client = genai.Client(api_key=api_key)

# Chat'i global olarak oluştur (sürekli konuşma için)
chat = client.chats.create(model="gemini-2.5-flash")

# --- Doküman yükleme ve chunking ---
with open("mydoc.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

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

# --- Embedding modeli ---
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
chunk_embeddings = model.encode(chunks)

# --- Arama Fonksiyonu ---
def search(query, top_k=3):
    query_emb = model.encode([query])
    sims = cosine_similarity(query_emb, chunk_embeddings)[0]
    
    # en yüksek similarity'leri seç
    top_idx = np.argsort(sims)[::-1][:top_k]
    
    results = []
    for idx in top_idx:
        results.append((chunks[idx], sims[idx]))
    
    return results

# --- Gradio için respond fonksiyonu ---
def respond(message: str, history: list[dict] | None = None) -> str:
    if not message:
        return "Yardım etmeye hazırım!"
    
    # 1) Dokümanlardan ilgili context bul
    search_results = search(message, top_k=3)
    
    # 2) Context'i birleştir
    context = "\n\n".join([f"[Kaynak {i+1}]:\n{text}" for i, (text, score) in enumerate(search_results)])
    
    # 3) Gemini'ye context ile birlikte mesaj gönder
    prompt = f"""Aşağıdaki kaynaklara dayanarak kullanıcının sorusunu cevapla:

{context}

Kullanıcı sorusu: {message}

Cevabını sadece verilen kaynaklara dayanarak ver. Eğer kaynaklarda bilgi yoksa, bunu belirt."""
    
    # 4) Chat üzerinden mesaj gönder (sürekli konuşma için)
    response = chat.send_message(prompt)
    
    return response.text

# --- Gradio arayüzü ---
starter_theme = gr.themes.Soft(primary_hue="cyan", neutral_hue="slate")

demo = gr.ChatInterface(
    fn=respond,
    type="messages",
    chatbot=gr.Chatbot(
        label="RAG Bootcamp Bot",
        height=400,
        placeholder="Bot cevapları burada gözükecek",
        show_copy_button=True,
        type="messages",
    ),
    textbox=gr.Textbox(
        label="Kullanıcı mesajı",
        placeholder="Dokümanlar hakkında soru sorun...",
        autofocus=True,
    ),
    title="Bootcamp RAG Sistemi",
    description=(
        "Bu bot dokümanlarınızı tarar ve Gemini AI ile cevap verir. "
        "Tüm konuşma aynı chat oturumunda devam eder."
    ),
    examples=["Atlas Synchron Dataworks ne yapıyor?", "Dokümanlar hakkında bilgi ver", "Önceki cevabını özetle"],
    theme=starter_theme
)

demo.launch(share=True)
