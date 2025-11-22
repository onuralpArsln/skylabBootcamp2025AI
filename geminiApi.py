
import os

from dotenv import load_dotenv
#python3.12 -m pip install python-dotenv

from google import genai
#python3.12 -m pip install google-genai

# .env dosyadanı yükle
load_dotenv()

# .env dosyadandan özel bilgileri al
api_key = os.getenv('GEMINI_API_KEY')

# google gemini istemcisini oluştur
client = genai.Client(api_key=api_key)

# 1) Bir chat başlat
chat = client.chats.create(
    model="gemini-2.5-flash"
)

# 2) Chate mesaj at ve cevabı response olarak kaydet 
response = chat.send_message("Explain how AI works in a few words")
# response cevabını ekrana yazdır
print(response.text)

# 3) Aynı chat üzerinde yeni mesaj at ve cevabı response olarak kaydet 
response = chat.send_message("Can you make it even shorter?")
# response cevabını ekrana yazdır
print(response.text)
