from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio

from pydantic import SecretStr
import os

api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

async def main():
    agent = Agent(
        task=(
            "What badge does stackoverflow award to users who meet with a stack exchange employee? Let's refer to this badge as x-badge"
            "Find user user835611 on StackOverflow. You can accept all cookies. What reputation score do they have?. "
            "Return a summary of topics they contribute to. "
            "Has user835611 earned x-badge? "
        ),
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
