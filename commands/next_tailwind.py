# commands/nextjs_tailwind.py
import webbrowser
import os
from pathlib import Path
from utils.installer import run_command, npm_install, install_tailwind_config
from utils.logger import Logger
from terminal.fs_commands import safe_mkdir


def create_nextjs_app(project_name: str) -> None:
    logger = Logger()
    logger.log(f"🚀 Creating Next.js + Tailwind project: {project_name}")

    # 1. Set default path → Desktop
    desktop_path = Path.home() / "OneDrive\Desktop"
    print(f"\n📂 Default location: {desktop_path}")
    custom = input("Want to change location? (y/N): ").strip().lower()

    if custom == "y":
        custom_path = input("Enter full directory path: ").strip()
        base_path = Path(custom_path).expanduser().resolve() if custom_path else desktop_path
    else:
        base_path = desktop_path

    # Final project path
    project_path = base_path / project_name
    
    if project_path.exists():
        logger.error(f"❌ Project directory already exists at: {project_path}")
        logger.error("Aborting to prevent overwriting existing files.")
        return

    safe_mkdir(project_path)

    # 2. Create Next.js app with Tailwind
    try:
        run_command(f"npx create-next-app@latest {project_name} --typescript --tailwind --eslint --app --src-dir --turbo --import-alias '@/*'", cwd=base_path)
    except Exception as e:
        logger.error(f"❌ Failed to create Next.js app: {e}")
        return

    # 3. Update app/page.tsx with the SHNK component
    page_tsx_path = project_path / "src" / "app" / "page.tsx"
    try:
        with open(page_tsx_path, "w", encoding='utf-8') as f:
            f.write("""'use client';

import React, { useState, useEffect } from 'react';

export default function SHNK() {
  const [isVisible, setIsVisible] = useState(false);
  const [completedSteps, setCompletedSteps] = useState(0);
  const [showCursor, setShowCursor] = useState(true);
  const [currentCommand, setCurrentCommand] = useState(0);

  const commands = [
    "$ thank you for choosing SHNK...",
    "$ installing Next.js framework...",
    "$ configuring Tailwind CSS...",
    "$ setup complete - happy coding!"
  ];

  const setupSteps = [
    { name: "Next.js", status: "complete" },
    { name: "Tailwind", status: "complete" },
    { name: "TypeScript", status: "complete" },
    { name: "ESLint", status: "complete" },
    { name: "App Router", status: "complete" }
  ];

  useEffect(() => {
    setIsVisible(true);
    
    // Command sequence
    const commandTimer = setInterval(() => {
      setCurrentCommand(prev => prev < commands.length - 1 ? prev + 1 : prev);
    }, 800);

    // Setup steps
    const stepTimer = setInterval(() => {
      setCompletedSteps(prev => prev < setupSteps.length ? prev + 1 : prev);
    }, 200);

    // Cursor blink
    const cursorTimer = setInterval(() => {
      setShowCursor(prev => !prev);
    }, 500);

    return () => {
      clearInterval(commandTimer);
      clearInterval(stepTimer);
      clearInterval(cursorTimer);
    };
  }, []);

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className={`max-w-4xl mx-auto transition-all duration-1000 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
        
        {/* Header */}
        <div className="text-center mb-16">
          <div className="mb-8">
            <pre className="text-white  text-lg leading-tight">
{`
 ███████╗██╗  ██╗███╗   ██╗██╗  ██╗
 ██╔════╝██║  ██║████╗  ██║██║ ██╔╝
 ███████╗███████║██╔██╗ ██║█████╔╝ 
 ╚════██║██╔══██║██║╚██╗██║██╔═██╗ 
 ███████║██║  ██║██║ ╚████║██║  ██╗
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
`}
            </pre>
          </div>
          
          <div className="inline-flex items-center justify-center w-12 h-12 border-2 border-white rounded-sm mb-6">
            <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
          </div>
          
          <h1 className="text-4xl font-light text-white mb-4 tracking-wide">
            Thank You
          </h1>
          
          <p className="text-lg text-gray-400 font-light">
            Your Next.js + Tailwind environment is ready
          </p>
        </div>

        {/* Terminal Command Output */}
        <div className="mb-16">
          <div className="bg-gray-950 border border-gray-800 rounded-lg p-6 font-mono text-sm">
            <div className="flex items-center mb-4">
              <div className="flex space-x-2">
                <div className="w-3 h-3 bg-gray-600 rounded-full"></div>
                <div className="w-3 h-3 bg-gray-600 rounded-full"></div>
                <div className="w-3 h-3 bg-gray-600 rounded-full"></div>
              </div>
              <div className="text-gray-500 text-xs ml-4">Terminal</div>
            </div>
            
            {commands.slice(0, currentCommand + 1).map((cmd, index) => (
              <div key={index} className="mb-2">
                <span className="text-gray-500">{cmd}</span>
                {index === currentCommand && showCursor && (
                  <span className="bg-white text-black ml-1 px-1">_</span>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Setup Progress */}
        <div className="mb-16">
          <div className="flex items-center justify-center mb-8">
            <div className="h-px bg-gray-800 flex-1"></div>
            <span className="px-6 text-sm text-gray-500 font-mono tracking-wider">INSTALLATION</span>
            <div className="h-px bg-gray-800 flex-1"></div>
          </div>
          
          <div className="max-w-3xl mx-auto">
            <div className="grid grid-cols-5 gap-6">
              {setupSteps.map((step, index) => (
                <div
                  key={index}
                  className={`text-center transition-all duration-500 ${
                    completedSteps > index ? 'opacity-100' : 'opacity-30'
                  }`}
                  style={{ transitionDelay: `${index * 100}ms` }}
                >
                  <div className={`w-12 h-12 mx-auto mb-3 border-2 rounded-sm flex items-center justify-center ${
                    completedSteps > index ? 'border-white bg-white' : 'border-gray-700'
                  }`}>
                    {completedSteps > index ? (
                      <svg className="w-6 h-6 text-black" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                      </svg>
                    ) : (
                      <div className="w-2 h-2 bg-gray-700 rounded-full"></div>
                    )}
                  </div>
                  <div className="text-xs text-gray-400 font-mono">{step.name}</div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Appreciation Message */}
        <div className="mb-16">
          <div className="max-w-2xl mx-auto text-center">
            <p className="text-gray-300 mb-6 leading-relaxed">
              Thanks for using SHNK to bootstrap your Next.js + Tailwind project. 
              This tool was crafted with care to make your development setup effortless.
            </p>
            <div className="flex items-center justify-center space-x-2 text-gray-500">
              <span className="text-sm font-mono">Made with</span>
              <span className="text-white text-lg">♡</span>
              <span className="text-sm font-mono">for developers</span>
            </div>
          </div>
        </div>

        {/* System Status */}
        <div className="mb-16">
          <div className="flex items-center justify-center mb-8">
            <div className="h-px bg-gray-800 flex-1"></div>
            <span className="px-6 text-sm text-gray-500 font-mono tracking-wider">STATUS</span>
            <div className="h-px bg-gray-800 flex-1"></div>
          </div>
          
          <div className="max-w-2xl mx-auto">
            <div className="bg-gray-950 border border-gray-800 rounded-lg p-6">
              <div className="grid grid-cols-3 gap-8 text-center">
                <div>
                  <div className="text-2xl font-light text-white mb-1">1.8s</div>
                  <div className="text-sm text-gray-500 font-mono">Setup Time</div>
                </div>
                <div className="border-l border-r border-gray-800">
                  <div className="text-2xl font-light text-white mb-1">Next.js + Tailwind</div>
                  <div className="text-sm text-gray-500 font-mono">Ready to Code</div>
                </div>
                <div>
                  <div className="text-2xl font-light text-white mb-1">✓</div>
                  <div className="text-sm text-gray-500 font-mono">Complete</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-16">
          <button className="bg-white hover:bg-gray-100 text-black font-medium py-3 px-8 rounded-sm transition-all duration-200 min-w-[160px]">
            Start Coding
          </button>
          
          <button className="bg-transparent border border-gray-700 hover:bg-gray-900 text-gray-200 font-medium py-3 px-8 rounded-sm transition-all duration-200 min-w-[160px]">
            View Docs
          </button>
        </div>

        {/* Support Section */}
        <div className="mb-16">
          <div className="max-w-2xl mx-auto bg-gray-950 border border-gray-800 rounded-lg p-6">
            <div className="text-center mb-4">
              <div className="text-gray-400 text-sm font-mono mb-2">Your next steps:</div>
              <div className="grid grid-cols-2 gap-4 text-sm font-mono">
                <div className="text-gray-500">npm run dev</div>
                <div className="text-gray-500">npm run build</div>
                <div className="text-gray-500">npm run start</div>
                <div className="text-gray-500">npm run lint</div>
              </div>
            </div>
            <div className="border-t border-gray-800 pt-4 text-center">
              <p className="text-gray-500 text-xs font-mono">
                Enjoying SHNK? Consider giving us a ⭐ on GitHub or sharing with fellow developers
              </p>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="border-t border-gray-800 pt-8">
          <div className="text-center">
            <p className="text-sm text-gray-500 mb-4 font-mono">
              SHNK v2.1.4 - Built by developers, for developers
            </p>
            
            <div className="flex justify-center space-x-8 text-sm mb-4">
              <a href="https://github.com/Ganesh-Sharmaz/shnk" className="text-gray-500 hover:text-white transition-colors duration-200 font-mono">
                ⭐ GitHub
              </a>
              <a href="#" className="text-gray-500 hover:text-white transition-colors duration-200 font-mono">
                📖 Docs
              </a>
              <a href="https://buymeacoffee.com/ganesh_sharmaz" className="text-gray-500 hover:text-white transition-colors duration-200 font-mono">
                💬 Support
              </a>
            </div>
            
            <p className="text-xs text-gray-600 font-mono">
              Open source • Community driven • Made with ♡
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}""")
        logger.success("✅ page.tsx updated with SHNK component.")
    except Exception as e:
        logger.error(f"❌ Could not update page.tsx: {e}")
    
    # 4. Install additional dependencies (if needed)
    logger.log("📦 Installing additional dependencies...")
    # Next.js with Tailwind is already configured during creation
    
    # 5. Start dev server and open browser
    logger.log("🧪 Starting development server...")
    try:
        # Open VS Code
        run_command("code .", cwd=project_path)
        
        # Open browser
        url = "http://localhost:3000"
        try:
            webbrowser.open(url)
            logger.success(f"🌐 Opened {url} in your default browser")
        except Exception as e:
            logger.warning(f"⚠️ Couldn't open browser automatically: {e}")
            logger.log(f"Please open this URL manually: {url}")
        
        # Start dev server
        run_command("npm run dev", cwd=project_path)
        
    except Exception as e:
        logger.error(f"❌ Failed to start dev server: {e}")