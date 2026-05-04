from dotenv import load_dotenv

load_dotenv()

from agent import build_agent
from pydantic_ai import Agent

agent: Agent = build_agent()
app = agent.to_web()

# def main()->None:
#     agent=build_agent()
#     while True:
#         user_input=input("Enter your command (or 'exit' to quit): ")
#         if user_input=='exit':
#             print("Goodbye!")
#             break
#         response=agent.run_sync(user_input)
#         print(f"Agent: {response.output}")

# if __name__ == "__main__":
#     main()