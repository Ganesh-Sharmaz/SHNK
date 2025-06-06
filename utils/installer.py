# utils/installer.py

import subprocess
from utils.logger import Logger

logger = Logger()


def run_command(command, cwd=None):
    """Run a shell command with optional working directory."""
    try:
        logger.log(f"$ {command}")
        subprocess.run(command, shell=True, check=True, cwd=cwd)
        logger.success("✓ Done.")
    except subprocess.CalledProcessError as e:
        logger.error(f"✗ Command failed: {e}")

def npm_init(project_path):
    run_command("npm init -y", cwd=project_path)

def npm_install(packages, project_path):
    if isinstance(packages, list):
        pkg_str = " ".join(packages)
    else:
        pkg_str = packages
    run_command(f"npm install {pkg_str}", cwd=project_path)

def install_tailwind_config(project_path):
    # Tailwind init command
    run_command("npx tailwindcss init -p", cwd=project_path)
