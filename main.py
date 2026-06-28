from dotenv import load_dotenv
from importlib.metadata import version

load_dotenv()

core_version = version("langchain-core")
lg_version = version("langgraph")
from langchain_groq import ChatGroq


print("Core version", core_version)
print("LangGraph version", lg_version)

def main():
    llm= ChatGroq(
        model_name= "openai/gpt-oss-20b",
        temperature= 0.5,
        max_tokens= 1024,
    )

    response = llm.invoke("Hello, how are you?")
    print(response)


if __name__ == "__main__":
    main()
