from UI.terminal import run_cli
from DataStorage.shelves import get_shelf_id, turn_into_shelf
import os
import dotenv
from rich.console import Console # Needed for error handling outside run_cli

console = Console()

dotenv.load_dotenv(".env",override=True)

API_KEY = os.getenv("API_KEY")

def main():
    try:
        DEFAULT_SHELF_NAME = "Default Collection"
        # Check if shelf exists
        shelf_id = get_shelf_id(DEFAULT_SHELF_NAME)
        
        if shelf_id is None:
            console.print(f"[yellow]Shelf '{DEFAULT_SHELF_NAME}' not found. Creating it now.[/yellow]")
            create_shelf(DEFAULT_SHELF_NAME)
            # After creation, retrieve the ID again (or rely on turn_into_shelf)
            shelf_id = get_shelf_id(DEFAULT_SHELF_NAME)
            
        shelf = turn_into_shelf(DEFAULT_SHELF_NAME)
        run_cli(shelf)
    except Exception as e:
        console.print(f"[bold red]Failed to initialize CLI: {e}[/bold red]")

if __name__ == "__main__":
    main()