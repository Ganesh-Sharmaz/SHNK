# 🚀 SHNK - A simple CLI tool for automating daily tasks of a developer

A safe, futuristic, and developer-focused terminal CLI built in Python that combines aesthetics with practical development utilities.

## ✨ Features

### 🛠️ Developer Tools
- **Project Scaffolding**
  - React + Tailwind CSS setup
  - Next.js + Tailwind CSS setup (coming soon)
  - Automated configuration and dependencies
  - Development server launch

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shnk.git
cd shnk
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## 🏗️ Project Structure
```
SHNK/
├── main.py                 # Application entry point
├── banner.py              # ASCII art and animations
├── commands/              # Project scaffolding commands
│   ├── react_tailwind.py
│   └── next_tailwind.py
├── terminal/              # Terminal functionality
│   ├── fs_commands.py
│   └── sandbox.py
├── utils/                 # Helper functions
│   ├── installer.py
│   └── logger.py
├── config/               # Configuration files
│   └── settings.json
├── assets/              # Static assets
│   └── ascii.txt
├── requirements.txt     # Project dependencies
└── README.md
```

## 🛠️ Development

### Building from Source
1. Install development dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development version:
```bash
python main.py
```

### Creating an Executable
```bash
pyinstaller SHNK.spec
```

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues
- Next.js project scaffolding is currently in development
- Some terminal commands are still being implemented

## 🔮 Roadmap
- [ ] Vue.js + Tailwind project scaffolding
- [ ] Express.js project setup
- [ ] Command autocomplete
- [ ] Custom themes support
- [ ] Plugin system

## 📫 Contact
Your Name - [@Ganesh_Sharmazz](https://x.com/Ganesh_Sharmazz)

Project Link: [https://github.com/Ganesh-Sharma/SHNK](https://github.com/Ganesh-Sharmaz/SHNK)
