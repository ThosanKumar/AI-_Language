@echo off
REM ---------------------------------------------------------------
REM  Language Tutor AI - one-click setup and run (Windows CMD)
REM  Double-click this file, or run:  setup_and_run.bat
REM ---------------------------------------------------------------
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    set PYCMD=py
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set PYCMD=python
    ) else (
        echo [ERROR] Python was not found. Install Python 3.12 or 3.13 from
        echo         https://www.python.org/downloads/windows/
        echo         and tick "Add python.exe to PATH" during installation.
        pause
        exit /b 1
    )
)

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    %PYCMD% -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Could not create the virtual environment.
        pause
        exit /b 1
    )
)

echo Installing / checking dependencies...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Dependency installation failed. See HOW_TO_RUN_WINDOWS.md.
    pause
    exit /b 1
)

if not exist ".streamlit\secrets.toml" (
    echo.
    echo [WARNING] .streamlit\secrets.toml was not found.
    echo           Copy .streamlit\secrets.toml.example to .streamlit\secrets.toml
    echo           and paste your Google AI Studio API key. The AI pages need it.
    echo.
)

echo Starting Language Tutor AI at http://localhost:8501  (Ctrl+C to stop)
".venv\Scripts\python.exe" -m streamlit run app.py
pause
