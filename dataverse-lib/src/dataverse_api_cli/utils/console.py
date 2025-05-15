"""Console utilities for rich text output."""

from rich.console import Console
from rich.table import Table
from rich import box

# Initialize Rich console for better output
console = Console()

def create_table(title: str, columns: list, box_style=box.ROUNDED) -> Table:
    """
    Create a Rich table with the given title and columns.
    
    Args:
        title (str): The table title
        columns (list): List of column names
        box_style: The box style for the table
        
    Returns:
        Table: A Rich table
    """
    table = Table(title=title, box=box_style)
    
    for column in columns:
        table.add_column(column)
        
    return table