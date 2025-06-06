#!/usr/bin/env python3
"""
SHNK Terminal - Professional Developer CLI
Main entry point for the application
"""

import os
import sys
from pathlib import Path
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.align import Align
from rich import print as rprint

# Import our modules
from banner import (
    display_banner, animate_welcome, display_loading_bar, display_section_divider,
    display_welcome_message, display_startup_sequence, get_color_scheme
)
from terminal.sandbox import TerminalSandbox
from commands.react_tailwind import create_react_app
from commands.next_tailwind import create_nextjs_app
from utils.logger import Logger

class SHNKTerminal:
    def __init__(self):
        self.console = Console()
        self.logger = Logger()
        self.sandbox = TerminalSandbox()
        self.current_path = self.sandbox.get_current_path()
        self.running = True
        self.color_scheme = get_color_scheme("professional")
        
    def show_main_menu(self):
        """Display the main developer menu with clean, professional styling"""
        display_section_divider("Main Menu")
        
        # Clean, professional table
        table = Table(
            show_header=True, 
            header_style=f"bold {self.color_scheme['primary']}",
            border_style=self.color_scheme['primary'],
            show_lines=False,
            pad_edge=False,
            box=None
        )
        
        table.add_column("Option", style=f"bold {self.color_scheme['primary']}", width=8, justify="center")
        table.add_column("Description", style="white", width=35)
        table.add_column("Status", style=f"{self.color_scheme['muted']}", width=12)
        
        # Clean menu options
        table.add_row("1", "Create React + Tailwind Project", "Available")
        table.add_row("2", "Create Next.js + Tailwind Project", "Available") 
        table.add_row("3", "Terminal Mode", "Coming Soon")
        table.add_row("4", "Settings", "Coming Soon")
        table.add_row("5", "Exit", "")
        
        self.console.print(table)
        self.console.print()
        
        # Simple instruction
        self.console.print(f"[{self.color_scheme['muted']}]Enter option number or type 'exit' to quit[/{self.color_scheme['muted']}]")
        self.console.print()
    
    def handle_project_creation(self, project_type):
        """Handle project scaffolding with professional UI"""
        display_section_divider(f"{project_type.title()} Project Setup")
        
        # Clean project info
        project_info = Panel(
            f"[bold {self.color_scheme['primary']}]{project_type.title()} + Tailwind CSS[/bold {self.color_scheme['primary']}]\n"
            f"[{self.color_scheme['muted']}]Modern development stack with best practices[/{self.color_scheme['muted']}]",
            border_style=self.color_scheme['primary'],
            padding=(0, 1),
            width=50
        )
        self.console.print(project_info)
        self.console.print()
        
        # Simple project name prompt
        project_name = Prompt.ask(
            f"[{self.color_scheme['primary']}]Project name[/{self.color_scheme['primary']}]",
            default="my-project"
        )
        
        if not project_name.strip():
            self.console.print("[red]Error: Project name cannot be empty[/red]")
            return
        
        # Validate project name
        if not project_name.replace("-", "").replace("_", "").isalnum():
            self.console.print("[red]Error: Invalid project name. Use letters, numbers, hyphens, or underscores only.[/red]")
            return
        
        # Show progress
        display_loading_bar(f"Creating {project_type} project", 1.5)
        
        try:
            if project_type == "react":
                create_react_app(project_name)
            elif project_type == "next":
                create_nextjs_app(project_name)
            
            # Success message
            success_panel = Panel(
                f"[bold {self.color_scheme['success']}]Project '{project_name}' created successfully[/bold {self.color_scheme['success']}]\n"
                f"[{self.color_scheme['muted']}]Location: ./workspace/{project_name}[/{self.color_scheme['muted']}]",
                border_style=self.color_scheme['success'],
                padding=(0, 1)
            )
            self.console.print(success_panel)
            
            # Ask about dev server
            self.console.print()
            start_server = Confirm.ask(
                f"[{self.color_scheme['accent']}]Start development server?[/{self.color_scheme['accent']}]",
                default=True
            )
            
            if start_server:
                display_loading_bar("Starting development server", 1.0)
                self.logger.info("Development server starting...")
                os.chdir(self.sandbox.workspace_path / project_name)
                os.system("npm run dev")
                    
        except Exception as e:
            # Clean error display
            error_panel = Panel(
                f"[bold red]Project creation failed[/bold red]\n"
                f"[{self.color_scheme['muted']}]{str(e)}[/{self.color_scheme['muted']}]",
                border_style="red",
                padding=(0, 1)
            )
            self.console.print(error_panel)
    
    def run(self):
        """Main application loop with professional interface"""
        try:
            # Clean startup
            display_startup_sequence()
            display_loading_bar("Initializing system", 1.5)
            
            # Status message
            self.console.print(f"[bold {self.color_scheme['success']}]System ready[/bold {self.color_scheme['success']}]")
            self.console.print()
            
            while self.running:
                try:
                    self.show_main_menu()
                    choice = Prompt.ask(
                        f"[{self.color_scheme['primary']}]Select option[/{self.color_scheme['primary']}]", 
                        choices=["1", "2", "3", "4", "5", "react", "next", "terminal", "settings", "exit"]
                    )
                    
                    if choice in ["1", "react"]:
                        self.handle_project_creation("react")
                    elif choice in ["2", "next"]:
                        self.handle_project_creation("next")
                    elif choice in ["3", "terminal"]:
                        self.console.print(f"[{self.color_scheme['warning']}]Terminal mode available in next update[/{self.color_scheme['warning']}]")
                    elif choice in ["4", "settings"]:
                        self.console.print(f"[{self.color_scheme['warning']}]Settings panel available in next update[/{self.color_scheme['warning']}]")
                    elif choice in ["5", "exit"]:
                        self.running = False
                    
                except KeyboardInterrupt:
                    self.console.print(f"\n[{self.color_scheme['muted']}]Use 'exit' to quit safely[/{self.color_scheme['muted']}]")
                except Exception as e:
                    self.console.print(f"[red]Error: {str(e)}[/red]")
        
        finally:
            # Clean goodbye
            display_section_divider("Shutdown")
            self.console.print(f"[{self.color_scheme['primary']}]Thank you for using SHNK[/{self.color_scheme['primary']}]")

def main():
    """Entry point"""
    terminal = SHNKTerminal()
    terminal.run()

if __name__ == "__main__":
    main()