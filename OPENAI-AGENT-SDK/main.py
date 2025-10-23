from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from decouple import config 

set_tracing_disabled(True)



key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")

gemini_client = AsyncOpenAI(
    api_key=key,
    base_url=base_url
)

MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client
)

agent = Agent(
    name="Helpful Assistant",
    instructions="You are a helpful and friendly assistant. Always respond politely, clearly, and try to give useful, accurate, and easy-to-understand answers to any question",
    model=MODEL
)


response = Runner.run_sync(
    starting_agent=agent, 
    input="Can you give me some tips to stay focused while studying?, Give me a short answer"
)

print(response.final_output)
