from api_secret import secret

from groq import Groq

client = Groq(
    api_key=secret,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "WHat is the most advanced thing you know in python",
        }
    ],
    model="llama-3.1-8b-instant",
)

print(chat_completion.choices[0].message.content)
