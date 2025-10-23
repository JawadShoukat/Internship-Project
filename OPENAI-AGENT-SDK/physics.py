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
    name="Physics Teacher",
    instructions="You are a Physics Teacher",
    model=MODEL
)

response = Runner.run_sync(
    starting_agent=agent,
    input="What is Phisics, give me a short answer"
)

print(response.final_output)