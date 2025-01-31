from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio

from pydantic import SecretStr
import os

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

async def main():
    agent = Agent(
        task=(
            "Open file:///Users/franzih/code/operator/users.txt. "
            "For every name in that list, find the user on StackOverflow. You can accept all cookies. What reputation score do they have?. "
            "Return a summary of topics they contribute to. "
        ),
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
