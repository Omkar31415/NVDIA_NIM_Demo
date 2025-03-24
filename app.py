from langchain_nvidia_ai_endpoints import ChatNVIDIA
import dotenv
import os

dotenv.load_dotenv()
NVDIA_API_KEY=os.getenv("NVDIA_API_KEY")

client = ChatNVIDIA(
  model="meta/llama3-70b-instruct",
  api_key=NVDIA_API_KEY, 
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
)

for chunk in client.stream([{"role":"user","content":"Provide me an article on Generative AI"}]): 
  print(chunk.content, end="")

