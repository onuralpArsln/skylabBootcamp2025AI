import gradio as gr


def respond(message: str, history: list[tuple[str, str]] | None = None) -> str:
    """
    Return a simple tutorial-friendly response to the user's message.

    Parameters
    ----------
    message:
        Latest user input from the chat box.
    history:
        Prior conversation turns supplied by Gradio. Unused here but kept
        for clarity so new learners can see where context would be provided.
    """
    if not message:
        return "I'm here when you're ready to chat!"

    # Keep the logic intentionally simple for bootcamp starters.
    return f"I heard you say: '{message}'. That's great! What would you like to try next?"


starter_theme = gr.themes.Soft(primary_hue="cyan", neutral_hue="slate")

demo = gr.ChatInterface(
    fn=respond,
    chatbot=gr.Chatbot(
        label="Bootcamp Bot",
        height=420,
        placeholder="Responses from the bot will show up here.",
        show_copy_button=True,
    ),
    textbox=gr.Textbox(
        label="Your message",
        placeholder="Try saying hello or ask what you can learn.",
        autofocus=True,
    ),
    title="Bootcamp Starter Chatbot",
    description=(
        "Type a message to see how the chatbot can read your input and reply. "
        "This demo keeps the logic simple so you can focus on learning Gradio."
    ),
    examples=["Hello there!", "What can I learn today?", "How does Gradio work?"],
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


if __name__ == "__main__":
    
    demo.launch()


