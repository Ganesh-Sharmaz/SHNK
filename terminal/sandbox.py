"""
FuturTerminal - Sandbox Environment
Handles safe file system operations within a sandboxed environment
"""

from pathlib import Path
from typing import Optional
import shutil
import os

class TerminalSandbox:
    def __init__(self, workspace_path: Optional[Path] = None):
        self.workspace_path = workspace_path or Path("./workspace").resolve()
        self.current_path = self.workspace_path
        
    def initialize(self) -> None:
        """Initialize the sandbox environment"""
        self.workspace_path.mkdir(exist_ok=True)
        
    def get_current_path(self) -> Path:
        """Get the current working directory"""
        return self.current_path
        
    def set_current_path(self, path: Path) -> None:
        """Set the current working directory"""
        if not str(path).startswith(str(self.workspace_path)):
            raise ValueError("Access denied: Path outside sandbox")
        self.current_path = path
        
    def sanitize_path(self, path: str) -> Path:
        """Ensure path stays within sandbox"""
        try:
            # Convert to absolute path within sandbox
            abs_path = (self.current_path / path).resolve()
            # Check if path is within sandbox
            if not str(abs_path).startswith(str(self.workspace_path)):
                raise ValueError("Access denied: Path outside sandbox")
            return abs_path
        except Exception as e:
            raise ValueError(f"Invalid path: {str(e)}")
            
    def cleanup(self) -> None:
        """Clean up the sandbox environment"""
        if self.workspace_path.exists():
            shutil.rmtree(self.workspace_path)
