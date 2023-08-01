from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

GPT_SYS_PROMPT = "Eres el Rick de Rick y Morty. Responderas todas los mensajes como lo hace Rick."
CHAT_HISTORY_LENGTH = 8

chat_history = []

def add_chat_history(gpt_user_prompt):
    if len(chat_history) > CHAT_HISTORY_LENGTH:
        del chat_history[0]
    chat_history.append(gpt_user_prompt)

def chat(gpt_user_prompt):
    add_chat_history({"role": "user", "content": gpt_user_prompt})
    prompt = chat_history.copy()
    prompt.insert(0, {"role": "system", "content": f"{GPT_SYS_PROMPT}"})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )
    gpt_assistant_answer = completion.choices[0].message.content

    add_chat_history({"role": "assistant", "content": gpt_assistant_answer})

    return gpt_assistant_answer

print("¡Realiza una pregunta a Rick!")
while True:
    user_message = input("Morty: ")
    chatgpt_message = chat(user_message)
    print("Rick: " + chatgpt_message)
