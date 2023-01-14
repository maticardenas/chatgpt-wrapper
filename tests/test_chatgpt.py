from chatgpt_wrapper import ChatGPT


def test_ask_headless_chat_gpt():
    chat_gpt = ChatGPT(headless=True)

    response = chat_gpt.ask("hello")

    assert response == "Hello! How can I help you today?\n"

