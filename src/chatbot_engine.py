from langchain.chat_models import ChatOpenAI
import langchain

langchain.verbose = True

def chat(message: str) -> str:
  llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
  return llm.predict(message)
