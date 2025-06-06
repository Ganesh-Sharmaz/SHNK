"""
FuturTerminal - Core Terminal Implementation
Handles command processing, history, and autocompletion
"""

import os
import sys
import shlex
from pathlib import Path
from typing import List, Dict, Optional, Callable
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import print as rprint

from .sandbox import TerminalSandbox
from .fs_commands import FileSystemCommands

class FuturTerminalCLI:
    def __init__(self, sandbox_path=None):
        self.console = Console()
        self.sandbox = TerminalSandbox(sandbox_path)
        self.fs = FileSystemCommands(self.sandbox)
        self.command_history: List[str] = []
        self.running = True
        
        # Command registry
        self.commands: Dict[str, Callable] = {
            'ls': self._cmd_ls,
            'cd': self._cmd_cd,
            'pwd': self._cmd_pwd,
            'mkdir': self._cmd_mkdir,
            'touch': self._cmd_touch,
            'cat': self._cmd_cat,
            'clear': self._cmd_clear,
            'help': self._cmd_help,
            'history': self._cmd_history,
            'tree': self._cmd_tree,
            'exit': self._cmd_exit
        }
        
        # Command aliases
        self.aliases: Dict[str, str] = {
            'dir': 'ls',
            'cls': 'clear',
            'quit': 'exit',
            '?': 'help'
        }
        
        # Command descriptions for help
        self.command_descriptions = {
            'ls': 'List directory contents',
            'cd': 'Change directory',
            'pwd': 'Print working directory',
            'mkdir': 'Create a new directory',
            'touch': 'Create an empty file',
            'cat': 'Display file contents',
            'clear': 'Clear the terminal screen',
            'help': 'Show this help message',
            'history': 'Show command history',
            'tree': 'Display directory structure',
            'exit': 'Exit the terminal'
        }

    def _get_prompt(self) -> str:
        """Generate the terminal prompt with current directory"""
        rel_path = self.sandbox.get_current_path().relative_to(self.sandbox.workspace_path)
        if rel_path == Path('.'):
            dir_name = '~'
        else:
            dir_name = rel_path.name
        return f"[bold cyan]futur[/bold cyan]:[bold blue]{dir_name}[/bold blue]$ "

    def _cmd_ls(self, args: List[str]) -> None:
        """List directory contents"""
        path = args[0] if args else None
        self.fs.list_directory(path)

    def _cmd_cd(self, args: List[str]) -> None:
        """Change directory"""
        path = args[0] if args else ""
        self.fs.change_directory(path)

    def _cmd_pwd(self, args: List[str]) -> None:
        """Print working directory"""
        try:
            rel_path = self.sandbox.get_current_path().relative_to(self.sandbox.workspace_path)
            self.console.print(f"[green]{rel_path}[/green]")
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")

    def _cmd_mkdir(self, args: List[str]) -> None:
        """Create a new directory"""
        if not args:
            self.console.print("[red]Error: Directory name required[/red]")
            return
        self.fs.create_directory(args[0])

    def _cmd_touch(self, args: List[str]) -> None:
        """Create an empty file"""
        if not args:
            self.console.print("[red]Error: File name required[/red]")
            return
        self.fs.create_file(args[0])

    def _cmd_cat(self, args: List[str]) -> None:
        """Display file contents"""
        if not args:
            self.console.print("[red]Error: File name required[/red]")
            return
        self.fs.read_file(args[0])

    def _cmd_clear(self, args: List[str]) -> None:
        """Clear the terminal screen"""
        self.console.clear()

    def _cmd_help(self, args: List[str]) -> None:
        """Show help message"""
        table = Table(title="Available Commands", show_header=True, header_style="bold green")
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="white")
        table.add_column("Aliases", style="yellow")
        
        for cmd, desc in self.command_descriptions.items():
            aliases = [alias for alias, cmd_name in self.aliases.items() if cmd_name == cmd]
            table.add_row(cmd, desc, ", ".join(aliases) if aliases else "")
        
        self.console.print(table)

    def _cmd_history(self, args: List[str]) -> None:
        """Show command history"""
        if not self.command_history:
            self.console.print("[yellow]No command history[/yellow]")
            return
        
        table = Table(title="Command History", show_header=True, header_style="bold green")
        table.add_column("No.", style="cyan")
        table.add_column("Command", style="white")
        
        for i, cmd in enumerate(self.command_history, 1):
            table.add_row(str(i), cmd)
        
        self.console.print(table)

    def _cmd_tree(self, args: List[str]) -> None:
        """Display directory structure"""
        path = args[0] if args else None
        self.fs.show_tree(path)

    def _cmd_exit(self, args: List[str]) -> None:
        """Exit the terminal"""
        self.running = False

    def _get_command_completions(self, text: str) -> List[str]:
        """Get command completions for autocomplete"""
        if not text:
            return list(self.commands.keys()) + list(self.aliases.keys())
        
        # Match commands and aliases
        matches = []
        for cmd in self.commands:
            if cmd.startswith(text):
                matches.append(cmd)
        for alias in self.aliases:
            if alias.startswith(text):
                matches.append(alias)
        
        return matches

    def _process_command(self, command: str) -> None:
        """Process a command string"""
        try:
            # Split command into parts
            parts = shlex.split(command)
            if not parts:
                return
            
            # Get command and arguments
            cmd = parts[0].lower()
            args = parts[1:]
            
            # Handle aliases
            if cmd in self.aliases:
                cmd = self.aliases[cmd]
            
            # Execute command
            if cmd in self.commands:
                self.commands[cmd](args)
            else:
                self.console.print(f"[red]Unknown command: {cmd}[/red]")
                self.console.print("Type 'help' for available commands")
            
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")

    def run(self) -> None:
        """Main terminal loop"""
        self.console.print(Panel.fit(
            "🔧 [bold cyan]Terminal Mode[/bold cyan]\n"
            "Safe sandbox environment - Type 'help' for commands\n"
            "Type 'menu' to return to main menu",
            border_style="cyan"
        ))
        
        while self.running:
            try:
                # Get command with autocomplete
                command = Prompt.ask(
                    self._get_prompt(),
                    completer=self._get_command_completions
                ).strip()
                
                if not command:
                    continue
                
                if command == "menu":
                    break
                
                # Add to history
                self.command_history.append(command)
                
                # Process command
                self._process_command(command)
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Use 'exit' to quit or 'menu' to return to main menu[/yellow]")
            except Exception as e:
                self.console.print(f"[red]Error: {str(e)}[/red]")

if __name__ == "__main__":
    # Test the terminal
    terminal = FuturTerminalCLI()
    terminal.run() 