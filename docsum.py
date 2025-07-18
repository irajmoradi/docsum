import os
from groq import Groq
import argparse
parser = argparse.ArgumentParser(prog='docsum')
parser.add_argument('file_name')
args = parser.parse_args()

filename = args.file_name
try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
except Exception as e:
    print(f"error {e} has occured")

client = Groq(
                
        api_key=os.environ.get("GROQ_API_KEY"),
        )
chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'system',
                'content': "Summarize the input below, limit to 1 paragraph with 17th  grade reading level",
                },
                {
                "role":"user",
                "content": content,
                }
            ],
        model = "llama3-8b-8192"
        )
print(chat_completion.choices[0].message.content)
