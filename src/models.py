from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

chatgpt_4o_mini = init_chat_model("openai:gpt-4o-mini")