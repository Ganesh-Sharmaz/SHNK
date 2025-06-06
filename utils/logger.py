from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
    "debug": "dim white"
})

console = Console(theme=custom_theme)

class Logger:
  def info(self, msg: str):
    console.print(f"[info][INFO][/info] {msg}")

  def success(self, msg: str):
      console.print(f"[success][✔ SUCCESS][/success] {msg}")
  
  def warning(self, msg: str):
      console.print(f"[warning][! WARNING][/warning] {msg}")
  
  def error(self, msg: str):
      console.print(f"[error][✘ ERROR][/error] {msg}")
  
  def debug(self, msg: str):
      console.print(f"[debug][DEBUG][/debug] {msg}")
  def log(self, msg: str):
      console.print(f"[info][INFO][/info] {msg}")
