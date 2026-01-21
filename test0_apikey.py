from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create (
    model = os.getenv("MODEL_NAME"),
    messages = [
        {"role" : "user", "content" : "이병헌으로 3행시 만들어 줘"}
        ],
)

print(response.choices[0].message.content)



# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# response = client.responses.create(
#     model="gpt-5-nano",
#     input="김범준으로 3행시 만들어 줘.",
#     store=True
# )

# print(response.output_text)