from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner, set_tracing_disabled
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
    name="Math's Teacher",
    instructions="You are a math teacher. Whenever someone asks you a question answer it like a real math teacher — explain clearly, step by step, and in a polite teaching tone",
    model=MODEL
)



response = Runner.run_sync(
    starting_agent=agent, 
    input="What is the sum of 45 and 27, Give me a short answer, give me a short answer"
)

print(response.final_output)
