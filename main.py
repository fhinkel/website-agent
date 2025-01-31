from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
load_dotenv()


async def main():

    # Configure Chrome profile instead of incognito window
    browser = Browser(
        config=BrowserConfig(
            chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            # chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --profile-directory=\"Profile 1\"'
            extra_chromium_args=['--profile-directory=Default'],
        )
    )

    agent = Agent(
        # task=("Go to google and search for MSFT stock."
        # "Open the first result but ignore Market Watch and Yahoo"
        # "Return a summary of why the stock dropped today"
        # "got back to google and open the next result"
        # "Return the title and a summary of why the stock dropped. Begin and end that summary with '------'"
        # ),
        # task=(
        #     "Use the profile for Franziska Hinkelmann. "
        #     "Got to reddit and find the username of Martin Omander. "
        #     "Find his post history for the last 60 days. "
        #     "Return his posts related to Google Cloud Platform (that includes products such as GKE, Kubernetes, Code Assist, Gemini, Vertix, Google Cloud, GCP, and others). "
        #     "Summarize his expertise in one paragraph starting with a line break and wrap the summary in ********. "
        #     "Find his top 3 comments with the most upvotes and list the title of the corresponding posts. "
        # ),
        task=(
            "What badge does stackoverflow award to users who meet with a stack exchange employee? Let's refer to this badge as x-badge"
            "Find user user835611 on StackOverflow. You can accept all cookies. What reputation score do they have?. "
            "Return a summary of topics they contribute to. "
            "Has user835611 earned x-badge? "
        ),
        llm=ChatOpenAI(model="gpt-4o"),
        # browser=browser,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
