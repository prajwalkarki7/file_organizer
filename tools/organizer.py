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
    def organize_directory(directory_path: str) -> str:
        """
        Scans a directory and automatically moves all files into folders 
        based on their types (PDFs, Docs, Images, etc.).
        """
        path = directory_path.strip().replace('"', '').replace('\\', '/')
        
        if not os.path.exists(path):
            return f"Error: The path '{path}' does not exist."

        moved_count = 0
        
        for filename in os.listdir(path):
            old_path = os.path.join(path, filename)
            
            if os.path.isdir(old_path):
                continue

            ext = os.path.splitext(filename)
            
            if ext == '.pdf':
                target_folder = "PDFs"
            elif ext in ['.doc', '.docx', '.txt']:
                target_folder = "Docs"
            elif ext in ['.jpg', '.png', '.jpeg', '.gif']:
                target_folder = "Images"
            elif ext in ['.py', '.env', '.gitignore']:
                target_folder = "Development"
            else:
                target_folder = "Other_Files"
            
            full_target_dir = os.path.join(path, target_folder)
            
            if not os.path.exists(full_target_dir):
                os.makedirs(full_target_dir)
            
            new_path = os.path.join(full_target_dir, filename)
            
            try:
                os.rename(old_path, new_path)
                moved_count += 1
            except Exception as e:
                continue

        return f"Success: Organized {moved_count} files in '{path}'."