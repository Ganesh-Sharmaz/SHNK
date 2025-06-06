"""
FuturTerminal - File System Commands
Implements safe file system operations for the terminal
"""

from pathlib import Path
from typing import List, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class FileSystemCommands:
    def __init__(self, sandbox):
        self.sandbox = sandbox
        self.console = Console()
        
    def list_directory(self, path: Optional[Path] = None) -> None:
        """List directory contents"""
        try:
            path = path or self.sandbox.get_current_path()
            if not path.is_dir():
                raise ValueError(f"Not a directory: {path}")
            
            # Create table for directory listing
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Type", style="cyan")
            table.add_column("Name", style="white")
            table.add_column("Size", style="green")
            
            # Add parent directory
            if path != self.sandbox.workspace_path:
                table.add_row("📁", "..", "")
            
            # List contents
            for item in sorted(path.iterdir()):
                if item.is_dir():
                    table.add_row("📁", item.name, "")
                else:
                    size = item.stat().st_size
                    size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.1f} KB"
                    table.add_row("📄", item.name, size_str)
            
            self.console.print(table)
            
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            
    def change_directory(self, path: str) -> None:
        """Change directory"""
        try:
            if not path:
                self.sandbox.set_current_path(self.sandbox.workspace_path)
                return
            
            new_path = self.sandbox.sanitize_path(path)
            if not new_path.is_dir():
                raise ValueError(f"Not a directory: {path}")
            
            self.sandbox.set_current_path(new_path)
            
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            
    def create_directory(self, path: str) -> None:
        """Create a new directory"""
        try:
            if not path:
                raise ValueError("Directory name required")
            
            new_path = self.sandbox.sanitize_path(path)
            if new_path.exists():
                raise ValueError(f"Path already exists: {path}")
            
            new_path.mkdir(parents=True)
            self.console.print(f"[green]Created directory: {new_path.name}[/green]")
            
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            
    def create_file(self, path: str) -> None:
        """Create an empty file"""
        try:
            if not path:
                raise ValueError("File name required")
            
            new_path = self.sandbox.sanitize_path(path)
            if new_path.exists():
                raise ValueError(f"File already exists: {path}")
            
            new_path.touch()
            self.console.print(f"[green]Created file: {new_path.name}[/green]")
            
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            
    def read_file(self, path: str) -> None:
        """Display file contents"""
        try:
            if not path:
                raise ValueError("File name required")
            
            file_path = self.sandbox.sanitize_path(path)
            if not file_path.is_file():
                raise ValueError(f"Not a file: {path}")
            
            content = file_path.read_text()
            self.console.print(Panel(content, title=file_path.name))
            
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            
    def show_tree(self, path: Optional[Path] = None) -> None:
        """Display directory structure"""
        try:
            path = path or self.sandbox.get_current_path()
            if not path.is_dir():
                raise ValueError(f"Not a directory: {path}")
            
            def _tree(p: Path, prefix: str = "", is_last: bool = True):
                # Skip hidden files and directories
                if p.name.startswith('.'):
                    return
                
                # Print current item
                marker = "└── " if is_last else "├── "
                self.console.print(f"{prefix}{marker}[cyan]{p.name}[/cyan]")
                
                # Print children
                if p.is_dir():
                    prefix += "    " if is_last else "│   "
                    children = sorted(p.iterdir())
                    for i, child in enumerate(children):
                        _tree(child, prefix, i == len(children) - 1)
            
            _tree(path)
            
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
def safe_mkdir(path: Path) -> None:
    """Safely create a directory if it doesn't exist"""
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        Console().print(f"[red]Error creating directory {path}: {str(e)}[/red]")