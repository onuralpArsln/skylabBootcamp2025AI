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
    theme=starter_theme,
    css="""
        .gradio-container {
           background: #001245;
           background: linear-gradient(90deg, rgba(0, 18, 69, 1) 0%, rgba(15, 23, 42, 1) 50%, rgba(0, 49, 184, 1) 100%);
        }

        .gradio-container .gr-button-primary {
            font-weight: 600;
        }

        .gradio-container .gr-textbox textarea {
            border-radius: 12px;
        }

        .gradio-container .gr-chatbot {
            border-radius: 16px;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
        }
    """,
)

demo.launch(share=True)
