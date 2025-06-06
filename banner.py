"""
SHNK - Banner and ASCII Art Module
Handles welcome screen, ASCII art, and animations with professional styling
"""

import time
import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich import print as rprint

console = Console()

SHNK_TERMINAL_ASCII = """
███████╗██╗  ██╗███╗   ██╗██╗  ██╗
██╔════╝██║  ██║████╗  ██║██║ ██╔╝
███████╗███████║██╔██╗ ██║█████╔╝ 
╚════██║██╔══██║██║╚██╗██║██╔═██╗ 
███████║██║  ██║██║ ╚████║██║  ██╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""

# Professional decorative elements
CLEAN_DIVIDER = "─" * 60
SECTION_DIVIDER = "═" * 50

def display_banner():
    """Display the main SHNK banner with professional styling"""
    console.clear()
    
    # Clean, professional ASCII art
    banner_text = Text(SHNK_TERMINAL_ASCII)
    banner_text.stylize("bold bright_blue", 0, len(SHNK_TERMINAL_ASCII))
    
    # Center the banner
    console.print(Align.center(banner_text))
    
    # Professional subtitle
    subtitle = Text("Developer Toolkit & Project Generator", style="dim white")
    console.print(Align.center(subtitle))
    console.print()
    
    # Clean info panel
    info_panel = Panel(
        "[bold blue]Version[/bold blue] 1.0.0    [bold blue]Author[/bold blue] Ganesh Sharma\n"
        "[dim]React • Next.js • Express • Tailwind CSS[/dim]",
        title="System Information",
        border_style="blue",
        width=50,
        padding=(0, 1)
    )
    console.print(Align.center(info_panel))
    console.print()

def animate_welcome():
    """Simple, professional loading sequence"""
    messages = [
        "Initializing SHNK...",
        "Loading development tools...",
        "Environment ready"
    ]
    
    for msg in messages:
        console.print(f"[dim cyan]• {msg}[/dim cyan]")
        time.sleep(0.3)
    
    console.print("\n[bold green]Ready for development[/bold green]")
    time.sleep(0.5)

def display_loading_bar(task_name: str, duration: float = 2.0):
    """Display a clean progress indicator"""
    from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
    
    with Progress(
        TextColumn("[blue]{task.description}"),
        BarColumn(bar_width=30, style="blue", complete_style="bright_blue"),
        "[progress.percentage]{task.percentage:>3.0f}%",
        console=console,
        transient=True
    ) as progress:
        
        task = progress.add_task(task_name, total=100)
        
        while not progress.finished:
            progress.update(task, advance=2)
            time.sleep(duration / 50)

def display_section_divider(text: str = ""):
    """Display a clean section divider"""
    if text:
        divider = f"── {text} " + "─" * (45 - len(text))
    else:
        divider = CLEAN_DIVIDER
    
    console.print(f"[dim blue]{divider}[/dim blue]")

def display_welcome_message():
    """Display a professional welcome message"""
    welcome_panel = Panel(
        "[bold blue]Welcome to SHNK[/bold blue]\n\n"
        "[white]Streamline your development workflow with professional tooling.\n"
        "Create React and Next.js projects with modern configurations.[/white]\n\n"
        "[dim]Select an option below to get started.[/dim]",
        title="Welcome",
        border_style="blue",
        padding=(1, 2),
        width=60
    )
    
    console.print(welcome_panel)
    console.print()

def display_startup_sequence():
    """Professional startup sequence"""
    display_banner()
    animate_welcome()
    display_welcome_message()

# Professional color schemes
COLOR_SCHEMES = {
    "professional": {
        "primary": "blue",
        "secondary": "bright_blue", 
        "accent": "cyan",
        "success": "green",
        "error": "red",
        "warning": "yellow",
        "muted": "dim white"
    },
    "corporate": {
        "primary": "bright_blue",
        "secondary": "blue",
        "accent": "white",
        "success": "bright_green",
        "error": "bright_red", 
        "warning": "bright_yellow",
        "muted": "dim"
    },
    "minimal": {
        "primary": "white",
        "secondary": "bright_white",
        "accent": "cyan",
        "success": "green",
        "error": "red",
        "warning": "yellow",
        "muted": "dim"
    }
}

def get_color_scheme(theme: str = "professional"):
    """Get color scheme for specified theme"""
    return COLOR_SCHEMES.get(theme, COLOR_SCHEMES["professional"])

if __name__ == "__main__":
    # Test the banner functions
    display_startup_sequence()