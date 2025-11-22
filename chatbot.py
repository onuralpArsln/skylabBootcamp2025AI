import gradio as gr   #hızlı chat arayüz kütüphanesi

# mesajları işleyen fonksiyon
def respond(message: str, history: list[dict] | None = None) -> str:   
    if not message:
        return "Yardım etmeye hazırım!"
    return f"Bu mesajı attınız: '{message}'. Başka ne yapmak istersiniz"


# tema oluşturma 
starter_theme = gr.themes.Soft(primary_hue="cyan", neutral_hue="slate")

# mesaj arayüzü ayarları
demo = gr.ChatInterface(
    fn=respond,
    type="messages", 
    chatbot=gr.Chatbot(
        label="Bootcamp Bot",
        height=400,
        placeholder="Bot cevapları burada gözükecek",
        show_copy_button=True,
        type="messages",  
    ),
    textbox=gr.Textbox(
        label="Kullanıcı mesajı",
        placeholder="Mesaj atarak kullanmaya başlayın.",
        autofocus=True,
    ),
    title="Bootcamp Temel Bot",
    description=(
        "Bir mesaj atarak sistemin nasıl çalıştığını görün. "
        "Bu gradio kullanımı için basit bir örnektir."
    ),
    examples=["Merhaba!", "Bugün ne yemek yapsam?", "Gradio nasıl çalışır?"],
    theme=starter_theme
)

demo.launch(share=True)
