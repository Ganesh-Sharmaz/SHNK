"""
SHNK - Banner and ASCII Art Module
Handles welcome screen, ASCII art, and animations
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

# Compact version
SHNK_COMPACT_ASCII = """
 ____  _   _ _   _ _  __
/ ___|| | | | \\ | | |/ /
\\___ \\| | | |  \\| | ' / 
 ___) | |_| | |\\  | . \\ 
|____/ \\___/|_| \\_|_|\\_\\
"""

# Cyber-style decorative elements
CYBER_BORDER = "═" * 80
CYBER_CORNER = "╔" + "═" * 78 + "╗"
CYBER_BOTTOM = "╚" + "═" * 78 + "╝"

def display_banner():
    """Display the main FuturTerminal banner"""
    console.clear()
    
    # Create colorful ASCII art
    banner_text = Text(SHNK_TERMINAL_ASCII)
    banner_text.stylize("bold cyan", 0, len(SHNK_TERMINAL_ASCII))
    
    # Add gradient effect
    lines = SHNK_TERMINAL_ASCII.split('\n')
    colors = ["bright_cyan", "cyan", "blue", "bright_blue", "magenta", "bright_magenta"]
    
    styled_banner = Text()
    for i, line in enumerate(lines):
        if line.strip():  # Skip empty lines
            color = colors[i % len(colors)]
            styled_banner.append(line + "\n", style=f"bold {color}")
        else:
            styled_banner.append("\n")
    
    # Center the banner (SHNK logo only)
    console.print(Align.center(styled_banner))
    
    # Add subtitle - keep centered
    subtitle = Text("All in one tool for developers", style="italic bright_white")
    console.print(Align.center(subtitle))
    console.print()
    
    # Add version and info - keep centered
    info_panel = Panel(
        "[bold green]Version:[/bold green] 1.0.0\n"
        "[bold yellow]Author:[/bold yellow] Ganesh Sharma\n"
        "[bold cyan]Features:[/bold cyan] React, Next.js, Express, Tailwind\n"
        "[bold magenta]Status:[/bold magenta] Ready for Development 🚀",
        title="[bold white]System Info[/bold white]",
        border_style="bright_blue",
        width=60
    )
    console.print(Align.center(info_panel))
    console.print()

def animate_welcome():
    """Animated welcome sequence"""
    messages = [
        "🔧 Initializing SHNK...",
        "🛠️  Loading developer tools...",
        "⚡ Powering up sandbox environment...",
        "✨ Ready for action!"
    ]
    
    for msg in messages:
        console.print(f"[bold cyan]{msg}[/bold cyan]")
        time.sleep(0.5)
    
    console.print("\n[bold green]🚀 Welcome to the future of development![/bold green]")
    time.sleep(1)

def display_loading_bar(task_name: str, duration: float = 2.0):
    """Display an animated loading bar"""
    from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
    
    with Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=40),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        console=console
    ) as progress:
        
        task = progress.add_task(task_name, total=100)
        
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(duration / 100)

def display_cyber_divider(text: str = ""):
    """Display a cyberpunk-style divider"""
    if text:
        divider = f"═══════════════ {text} ═══════════════"
    else:
        divider = "═" * 60
    
    console.print(f"[bold cyan]{divider}[/bold cyan]")

def typewriter_effect(text: str, delay: float = 0.05):
    """Display text with typewriter effect"""
    for char in text:
        console.print(char, end="")
        time.sleep(delay)
    console.print()  # New line at the end

def display_matrix_effect():
    """Simple matrix-like effect for terminal startup"""
    import random
    
    matrix_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZアイウエオカキクケコサシスセソタチツテト"
    
    for _ in range(5):  # 5 lines of matrix effect
        line = ""
        for _ in range(80):
            line += random.choice(matrix_chars)
        
        console.print(f"[bold green]{line}[/bold green]")
        time.sleep(0.1)
    
    # Clear the matrix effect
    console.clear()

def display_welcome_message():
    """Display a styled welcome message - left aligned"""
    welcome_panel = Panel.fit(
        "[bold cyan]Welcome to SHNK![/bold cyan]\n\n"
        "🎯 [bold white]Purpose:[/bold white] Streamline your development workflow\n"
        "🛡️  [bold white]Safety:[/bold white] Sandboxed environment \n"
        "⚡ [bold white]Speed:[/bold white] Scaffold projects in seconds\n"
        "🎨 [bold white]Style:[/bold white] Beautiful terminal experience\n\n"
        "[italic bright_yellow]Let's build the future, one project at a time![/italic bright_yellow]",
        title="[bold magenta]🚀 SHNK TERMINAL 🚀[/bold magenta]",
        border_style="bright_cyan",
        padding=(1, 2)
    )
    
    console.print(welcome_panel)
    console.print()

def display_startup_sequence():
    """Complete startup sequence with animations"""
    if console.is_terminal:
        # Only show matrix effect in actual terminal
        display_matrix_effect()
    
    display_banner()
    animate_welcome()
    display_welcome_message()

# Color schemes for different themes
COLOR_SCHEMES = {
    "cyberpunk": {
        "primary": "bright_cyan",
        "secondary": "bright_magenta",
        "accent": "bright_yellow",
        "success": "bright_green",
        "error": "bright_red",
        "warning": "bright_yellow"
    },
    "matrix": {
        "primary": "bright_green",
        "secondary": "green",
        "accent": "bright_white",
        "success": "bright_green",
        "error": "bright_red",
        "warning": "bright_yellow"
    },
    "neon": {
        "primary": "bright_magenta",
        "secondary": "bright_blue",
        "accent": "bright_cyan",
        "success": "bright_green",
        "error": "bright_red",
        "warning": "bright_yellow"
    }
}

def get_color_scheme(theme: str = "cyberpunk"):
    """Get color scheme for specified theme"""
    return COLOR_SCHEMES.get(theme, COLOR_SCHEMES["cyberpunk"])

if __name__ == "__main__":
    # Test the banner functions
    display_startup_sequence()