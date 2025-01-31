
# Demo for browser_use with Gemini

```
pip install browser_use
export GEMINI_API_KEY=your_key
python main.py 
```

Create a Gemini Api key at [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)


This example uses Gemini 2.0 to control a Chrome browser. The code provided showcases how to:

* **Initialize a Chrome browser instance:**  Including configuring Chrome to use a specific profile.
* **Define tasks for the agent:**  Provide natural language instructions to the agent to specify the actions it should perform in the browser.
* **Utilize an LLM:**  Integrate with a large language model (in this case, the Gemini 2.0 model) to interpret instructions and guide the agent's actions.
* **Execute the agent:** Run the agent and observe the results of its browser interactions.

This specific example explores retrieving information from websites like Reddit and Stack Overflow by providing natural language queries to the agent. It highlights Gemini's capability to understand complex instructions, navigate websites, extract data, and summarize findings.


