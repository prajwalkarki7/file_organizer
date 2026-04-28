from pydantic_ai import Agent
from tools.organizer import register_organizer_tool
from pydantic_ai.models.groq import GroqModel

SYSTEM_PROMPT = """
You are a helpful assistant that can perform various file organization tasks such as creating folders, moving files, and listing files in a directory. You have access to the following tools:
1. get_file_type(file_name: str) -> str: Get the file type based on the file extension.
2. get_all_files_in_directory(directory: str) -> list: Get a list of all files in the specified directory.
3. create_folder(folder_name: str) -> str: Create a new folder with the specified name.
4. move_file(file_name: str, destination_folder: str) -> str: Move a file to the specified destination folder.  

use these tools to help users organize their files effectively. Always provide clear and concise responses, and ensure that you handle any errors gracefully.

"You are a File Automation Executive. "
"When a user provides a directory path, you MUST call the 'organize_files' tool immediately. "
"Do not explain that you cannot move files; the 'organize_files' tool handles the actual moving. "
"Once the tool returns a success message, relay that message to the user."

"""

def build_agent(model_name:str="llama-3.3-70b-versatile") ->Agent:
    model=GroqModel(model_name=model_name)
    agent=Agent(model=model,system_prompt=SYSTEM_PROMPT)
    register_organizer_tool(agent)
    return agent
