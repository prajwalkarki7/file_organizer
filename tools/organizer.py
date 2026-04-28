from pydantic_ai import Agent
import os

def register_organizer_tool(agent: Agent)->None:
    @agent.tool_plain
    def get_file_type(file_name: str) -> str:
        """Get the file type based on the file extension."""
        if '.' in file_name:
            return file_name.rsplit('.', 1)[-1].lower()
        return 'unknown'
    
    @agent.tool_plain
    def get_all_files_in_directory(directory: str) -> list:
        """Get a list of all files in the specified directory."""
        import os
        try:
            return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        except Exception as e:
            return [str(e)]
    
    @agent.tool_plain
    def create_folder(folder_name: str) -> str:
        """Create a new folder with the specified name."""
        import os
        try:
            os.makedirs(folder_name, exist_ok=True)
            return f"Folder '{folder_name}' created successfully."
        except Exception as e:
            return str(e)
    
    @agent.tool_plain
    def move_file(file_name: str, destination_folder: str) -> str:
        """Move a file to the specified destination folder."""
        import os
        import shutil
        try:
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(file_name, destination_folder)
            return f"File '{file_name}' moved to '{destination_folder}' successfully."
        except Exception as e:
            return str(e)