#!/usr/bin/env python3
"""
FuturTerminal - A futuristic developer-focused terminal CLI
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
    display_banner, animate_welcome, display_loading_bar, display_cyber_divider, 
    typewriter_effect, display_welcome_message, display_startup_sequence,
    get_color_scheme, CYBER_BORDER, CYBER_CORNER, CYBER_BOTTOM
)
from terminal.sandbox import TerminalSandbox
from commands.react_tailwind import create_react_app
# from commands.next_tailwind import setup_next_tailwind
from utils.logger import Logger

class FuturTerminal:
    def __init__(self):
        self.console = Console()
        self.logger = Logger()
        self.sandbox = TerminalSandbox()
        self.current_path = self.sandbox.get_current_path()
        self.running = True
        self.color_scheme = get_color_scheme("cyberpunk")
        
        # Load configuration
        # self.config = self.load_config()
        
    # def load_config(self):
    #     """Load terminal configuration"""
    #     config_path = Path("config/settings.json")
    #     if config_path.exists():
    #         with open(config_path, 'r') as f:
    #             return json.load(f)
    #     return {
    #         "theme": "cyberpunk",
    #         "show_animations": True,
    #         "workspace_path": "./workspace"
    #     }
    
    # def save_config(self):
    #     """Save current configuration"""
    #     config_path = Path("config/settings.json")
    #     config_path.parent.mkdir(exist_ok=True)
    #     with open(config_path, 'w') as f:
    #         json.dump(self.config, f, indent=2)
    
    def show_main_menu(self):
        """Display the main developer menu with enhanced styling"""
        # Clear and add cyber divider
        display_cyber_divider("MAIN CONTROL PANEL")
        
        # Create enhanced table with cyberpunk styling
        table = Table(
            title="🚀 [bold bright_cyan]SHNK - DEVELOPER COMMAND CENTER[/bold bright_cyan] 🚀", 
            show_header=True, 
            header_style=f"bold {self.color_scheme['secondary']}",
            border_style=self.color_scheme['primary'],
            title_style=f"bold {self.color_scheme['accent']}"
        )
        
        table.add_column("🎯 Option", style=f"bold {self.color_scheme['primary']}", no_wrap=True, width=8)
        table.add_column("📋 Description", style="bright_white", width=35)
        table.add_column("⚡ Command", style=f"bold {self.color_scheme['success']}", width=15)
        table.add_column("🎨 Status", style=f"{self.color_scheme['accent']}", width=12)
        
        # Enhanced menu options with emojis and status
        table.add_row("1", "🎨 Create React + Tailwind Project", "react", "✅ Ready")
        table.add_row("2", "⚡ Create Next.js + Tailwind Project", "next", "🔧 Coming Soon")
        table.add_row("3", "💻 Enter Terminal Mode", "terminal", "🔧 Coming Soon")
        table.add_row("4", "⚙️  Settings & Configuration", "settings", "🔧 Coming Soon")
        table.add_row("5", "🚪 Exit SHNK", "exit", "🔴 Shutdown")
        
        # Display the table
        self.console.print(table)
        
        # Add decorative footer
        footer_panel = Panel(
            f"[{self.color_scheme['accent']}]💡 Tip:[/{self.color_scheme['accent']}] [bright_white]Type number or command name | "
            f"[{self.color_scheme['primary']}]Ctrl+C[/{self.color_scheme['primary']}] for help[/bright_white]",
            style=f"dim {self.color_scheme['primary']}",
            width=80
        )
        self.console.print(footer_panel)
        self.console.print()
    
    def handle_project_creation(self, project_type):
        """Handle project scaffolding with enhanced UI"""
        # Clear screen and show project creation header
        display_cyber_divider(f"{project_type.upper()} PROJECT CREATOR")
        
        # Create project info panel
        project_info = Panel.fit(
            f"[bold {self.color_scheme['primary']}]🚀 {project_type.title()} Project Setup[/bold {self.color_scheme['primary']}]\n\n"
            f"[{self.color_scheme['accent']}]📦 Stack:[/{self.color_scheme['accent']}] {project_type.title()} + Tailwind CSS\n"
            f"[{self.color_scheme['accent']}]🛡️  Environment:[/{self.color_scheme['accent']}] Sandboxed Development\n"
            f"[{self.color_scheme['accent']}]⚡ Speed:[/{self.color_scheme['accent']}] Rapid Scaffolding",
            title=f"[bold {self.color_scheme['secondary']}]PROJECT CONFIGURATION[/bold {self.color_scheme['secondary']}]",
            border_style=self.color_scheme['primary']
        )
        self.console.print(project_info)
        self.console.print()
        
        # Enhanced project name prompt
        typewriter_effect("📁 Enter your project name:", 0.03)
        project_name = Prompt.ask(
            f"[bold {self.color_scheme['primary']}]Project Name[/bold {self.color_scheme['primary']}]",
            default="my-awesome-project"
        )
        
        if not project_name.strip():
            self.logger.error("❌ Project name cannot be empty!")
            return
        
        # Validate project name with enhanced feedback
        if not project_name.replace("-", "").replace("_", "").isalnum():
            error_panel = Panel(
                f"[bold red]❌ INVALID PROJECT NAME[/bold red]\n\n"
                f"[yellow]Rules:[/yellow]\n"
                f"• Only letters, numbers, hyphens (-), and underscores (_)\n"
                f"• No spaces or special characters\n"
                f"• Example: my-react-app, awesome_project",
                title="[bold red]VALIDATION ERROR[/bold red]",
                border_style="red"
            )
            self.console.print(error_panel)
            return
        
        # Show creation progress
        display_loading_bar(f"🔧 Creating {project_type} project: {project_name}", 1.5)
        
        try:
            if project_type == "react":
                create_react_app(project_name)
            elif project_type == "next":
                setup_next_tailwind(project_name, self.sandbox.workspace_path)
            
            # Success message with animation
            success_panel = Panel.fit(
                f"[bold {self.color_scheme['success']}]✨ SUCCESS! ✨[/bold {self.color_scheme['success']}]\n\n"
                f"[bright_white]Project '[bold {self.color_scheme['accent']}]{project_name}[/bold {self.color_scheme['accent']}]' created successfully![/bright_white]\n"
                f"[dim]Location: ./workspace/{project_name}[/dim]",
                title=f"[bold {self.color_scheme['success']}]🎉 PROJECT READY 🎉[/bold {self.color_scheme['success']}]",
                border_style=self.color_scheme['success']
            )
            self.console.print(success_panel)
            
            # Ask if user wants to start dev server with enhanced styling
            self.console.print()
            start_server = Confirm.ask(
                f"[bold {self.color_scheme['accent']}]🚀 Start development server?[/bold {self.color_scheme['accent']}]",
                default=True
            )
            
            if start_server:
                display_loading_bar("⚡ Starting development server...", 1.0)
                self.logger.info("🌐 Development server starting...")
                os.chdir(self.sandbox.workspace_path / project_name)
                if project_type == "react":
                    os.system("npm start")
                else:
                    os.system("npm run dev")
                    
        except Exception as e:
            # Enhanced error display
            error_panel = Panel(
                f"[bold red]❌ PROJECT CREATION FAILED[/bold red]\n\n"
                f"[yellow]Error Details:[/yellow]\n{str(e)}\n\n"
                f"[dim]Please check your system configuration and try again.[/dim]",
                title="[bold red]⚠️  SYSTEM ERROR ⚠️[/bold red]",
                border_style="red"
            )
            self.console.print(error_panel)
    
    # def terminal_mode(self):
    #     """Enter interactive terminal mode with enhanced UI"""
    #     display_cyber_divider("TERMINAL SANDBOX MODE")
    #     
    #     terminal_panel = Panel.fit(
    #         f"[bold {self.color_scheme['primary']}]🔧 TERMINAL MODE ACTIVATED[/bold {self.color_scheme['primary']}]\n\n"
    #         f"[{self.color_scheme['accent']}]🛡️  Environment:[/{self.color_scheme['accent']}] Safe Sandbox\n"
    #         f"[{self.color_scheme['accent']}]💻 Commands:[/{self.color_scheme['accent']}] Type 'help' for available commands\n"
    #         f"[{self.color_scheme['accent']}]🔙 Return:[/{self.color_scheme['accent']}] Type 'menu' to return to main menu\n"
    #         f"[{self.color_scheme['accent']}]🚪 Exit:[/{self.color_scheme['accent']}] Type 'exit' to quit",
    #         title=f"[bold {self.color_scheme['secondary']}]SANDBOX TERMINAL[/bold {self.color_scheme['secondary']}]",
    #         border_style=self.color_scheme['primary']
    #     )
                #     self.console.print(terminal_panel)
    #     self.console.print()
        
    #     while self.running:
    #         try:
    #             # Enhanced prompt with current directory
    #             current_dir = self.sandbox.get_current_path().name
    #             prompt_text = f"[bold {self.color_scheme['primary']}]futur[/bold {self.color_scheme['primary']}]:[bold {self.color_scheme['secondary']}]{current_dir}[/bold {self.color_scheme['secondary']}]$ "
                
    #             command = Prompt.ask(prompt_text).strip()
                
    #             if not command:
    #                 continue
                
    #             if command == "menu":
    #                 break
    #             elif command == "exit":
    #                 self.running = False
    #                 break
    #             elif command == "help":
    #                 self.show_terminal_help()
    #             else:
    #                 self.sandbox.execute_command(command)
                    
    #         except KeyboardInterrupt:
    #             self.console.print(f"\n[{self.color_scheme['warning']}]💡 Use 'exit' to quit or 'menu' to return to main menu[/{self.color_scheme['warning']}]")
    #         except Exception as e:
    #             self.logger.error(f"Command error: {str(e)}")
    
    # def show_terminal_help(self):
    #     """Show available terminal commands with enhanced styling"""
    #     display_cyber_divider("TERMINAL COMMAND REFERENCE")
    #     
    #     help_table = Table(
    #         title=f"[bold {self.color_scheme['primary']}]📚 AVAILABLE COMMANDS 📚[/bold {self.color_scheme['primary']}]", 
    #         show_header=True, 
    #         header_style=f"bold {self.color_scheme['secondary']}",
    #         border_style=self.color_scheme['primary']
    #     )
    #     help_table.add_column("🔧 Command", style=f"bold {self.color_scheme['primary']}")
    #     help_table.add_column("📋 Description", style="bright_white")
    #     help_table.add_column("💡 Example", style=f"{self.color_scheme['accent']}")
        
    #     commands = [
    #         ("ls", "List directory contents", "ls"),
    #         ("pwd", "Show current directory", "pwd"),
    #         ("cd <dir>", "Change directory", "cd myproject"),
    #         ("mkdir <dir>", "Create directory", "mkdir newfolder"),
    #         ("touch <file>", "Create empty file", "touch index.html"),
    #         ("cat <file>", "Display file contents", "cat package.json"),
    #         ("tree", "Show directory tree", "tree"),
    #         ("clear", "Clear terminal screen", "clear"),
    #         ("menu", "Return to main menu", "menu"),
    #         ("exit", "Exit terminal", "exit"),
    #     ]
        
    #     for cmd, desc, example in commands:
    #         help_table.add_row(cmd, desc, example)
        
    #     self.console.print(help_table)
    
    # def show_settings(self):
    #     """Show and modify settings with enhanced styling"""
    #     display_cyber_divider("SYSTEM CONFIGURATION")
    #     
    #     settings_table = Table(
    #         title=f"[bold {self.color_scheme['accent']}]⚙️  SYSTEM SETTINGS ⚙️[/bold {self.color_scheme['accent']}]", 
    #         show_header=True, 
    #         header_style=f"bold {self.color_scheme['secondary']}",
    #         border_style=self.color_scheme['primary']
    #     )
    #     settings_table.add_column("🔧 Setting", style=f"bold {self.color_scheme['primary']}")
    #     settings_table.add_column("📊 Current Value", style="bright_white")
    #     settings_table.add_column("🎯 Status", style=f"{self.color_scheme['success']}")
        
    #     settings_table.add_row("Theme", self.config["theme"], "✅ Active")
    #     settings_table.add_row("Show Animations", str(self.config["show_animations"]), "✅ Enabled")
    #     settings_table.add_row("Workspace Path", str(self.config["workspace_path"]), "✅ Configured")
        
    #     self.console.print(settings_table)
    #     
    #     future_panel = Panel(
    #         f"[{self.color_scheme['accent']}]🚧 COMING SOON 🚧[/{self.color_scheme['accent']}]\n\n"
    #         f"[bright_white]• Theme switching (Cyberpunk, Matrix, Neon)\n"
    #         f"• Animation controls\n"
    #         f"• Custom workspace paths\n"
    #         f"• Export/Import configurations[/bright_white]",
    #         title=f"[bold {self.color_scheme['warning']}]FUTURE FEATURES[/bold {self.color_scheme['warning']}]",
    #         border_style=self.color_scheme['warning']
    #     )
    #     self.console.print(future_panel)
    
    def run(self):
        """Main application loop with enhanced startup sequence"""
        try:
            # Enhanced startup sequence
            display_startup_sequence()
            display_loading_bar("🔧 Initializing SHNK systems...", 2.0)
            
            # Initialize sandbox
            # self.sandbox.initialize()
            
            # Welcome message after startup
            welcome_panel = Panel.fit(
                f"[bold {self.color_scheme['success']}]🎉 SHNK TERMINAL READY 🎉[/bold {self.color_scheme['success']}]\n\n"
                f"[bright_white]All systems online and ready for development![/bright_white]\n"
                f"[dim]Choose an option from the menu below to get started.[/dim]",
                title=f"[bold {self.color_scheme['primary']}]SYSTEM STATUS[/bold {self.color_scheme['primary']}]",
                border_style=self.color_scheme['success']
            )
            self.console.print(welcome_panel)
            self.console.print()
            
            while self.running:
                try:
                    self.show_main_menu()
                    choice = Prompt.ask(
                        f"[bold {self.color_scheme['primary']}]Select your command[/bold {self.color_scheme['primary']}]", 
                        choices=["1", "2", "3", "4", "5", "react", "next", "terminal", "settings", "exit"]
                    )
                    
                    if choice in ["1", "react"]:
                        self.handle_project_creation("react")
                    elif choice in ["2", "next"]:
                        self.handle_project_creation("next")
                    elif choice in ["3", "terminal"]:
                        # self.terminal_mode()
                        typewriter_effect("🔧 Terminal mode coming soon in next update!", 0.05)
                    elif choice in ["4", "settings"]:
                        # self.show_settings()
                        typewriter_effect("⚙️ Settings panel coming soon in next update!", 0.05)
                    elif choice in ["5", "exit"]:
                        self.running = False
                    
                except KeyboardInterrupt:
                    self.console.print(f"\n[{self.color_scheme['warning']}]💡 Use option 5 or 'exit' to quit safely[/{self.color_scheme['warning']}]")
                except Exception as e:
                    error_panel = Panel(
                        f"[bold red]⚠️  MENU ERROR ⚠️[/bold red]\n\n"
                        f"[yellow]Error:[/yellow] {str(e)}\n"
                        f"[dim]Please try again or restart the application.[/dim]",
                        border_style="red"
                    )
                    self.console.print(error_panel)
        
        finally:
            # Enhanced goodbye message
            display_cyber_divider("SHUTDOWN SEQUENCE")
            goodbye_panel = Panel.fit(
                f"[bold {self.color_scheme['primary']}]🚀 SHNK TERMINAL SHUTDOWN 🚀[/bold {self.color_scheme['primary']}]\n\n"
                f"[bright_white]Thank you for using SHNK![/bright_white]\n"
                f"[{self.color_scheme['accent']}]Keep building the future! 🌟[/{self.color_scheme['accent']}]",
                title=f"[bold {self.color_scheme['secondary']}]GOODBYE[/bold {self.color_scheme['secondary']}]",
                border_style=self.color_scheme['primary']
            )
            self.console.print(goodbye_panel)
            typewriter_effect("System shutdown complete. See you next time! 👋", 0.03)
            # self.save_config()

def main():
    """Entry point"""
    terminal = FuturTerminal()
    terminal.run()

if __name__ == "__main__":
    main()