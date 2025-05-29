import os

from dotenv import load_dotenv, dotenv_values
from langchain_core.messages import SystemMessage, HumanMessage

from src.models import chatgpt_4o_mini
from src.utils import get_root_path


messages = [
    SystemMessage("You are an expert in polish civil law. Answer the following question."),
    HumanMessage("Czym jest Causa concurrens?"),
]
model = chatgpt_4o_mini
response = model.invoke(messages)
print(response.content)