from dotenv import load_dotenv
import os
from google import genai

load_dotenv()  # 自动加载 .env 文件中的变量
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)