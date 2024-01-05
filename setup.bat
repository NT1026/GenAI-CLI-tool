@echo off

set tab=    

echo:
echo ===================================
echo This is GenAI CLI-tool setup script.
echo ===================================
echo:
timeout /t 1 >NUL

echo:
echo Start Installation...
timeout /t 3 >NUL


:: A. Check if Python, Pip, and Virtualenv is existed
echo:
echo A. Check if Python, Pip, and Virtualenv is existed...
echo:
timeout /t 1 >NUL

:: A-1. Check if Python is existed.
python --version >NUL 2>NUL
if ERRORLEVEL 1 (
    echo %tab%* Installation FAILED *
    echo %tab%* Please install Python/Python3 first *
    timeout /t -1 >NUL
    exit
)
echo %tab%A-1. You have installed Python!
timeout /t 1 >NUL

:: A-2. Check if Pip is existed.
pip --version >NUL 2>NUL
if ERRORLEVEL 1 (
    echo %tab%* Installation FAILED *
    echo %tab%* Please install Pip/Pip3 first *
    timeout /t -1 >NUL
    exit
)
echo %tab%A-2. You have installed Pip!
timeout /t 1 >NUL

:: A-3. Check if Virtualenv is existed.
python -m virtualenv --version >NUL 2>NUL
if ERRORLEVEL 1 (
    pip install virtualenv >NUL 2>NUL
)
echo %tab%A-3. You have installed Virtualenv!
timeout /t 1 >NUL


:: B. Create virtual envirenments
echo:
echo B. Create virtual envirenments...
echo:
timeout /t 1 >NUL

:: B-1. Create virtual envirenments
python -m virtualenv .venv >NUL 2>NUL
echo %tab%B-1. Virtual envirenments (.venv) is created!
timeout /t 1 >NUL

:: B-2. Download necessary python package into venv
%cd%\.venv\Scripts\pip install -r requirements.txt >NUL 2>NUL
echo %tab%B-2. Necessary python packages in requirements.txt are all installed.
timeout /t 1 >NUL


:: C. Other configurations
echo:
echo C. Set other configurations
echo:
timeout /t 1 >NUL

:: C-1. Set scripts/configs.py
echo DOTENV_FILEPATH = "%cd%\.env" > scripts\configs.py
echo %tab%C-1. Setting scripts/configs.py...Success!
timeout /t 1 >NUL

:: C-2 Set .env
echo %tab%C-2. Setting API key created in MakerSuite (https://makersuite.google.com/app/apikey)...
timeout /t 1 >NUL

echo:
set /p apikey= Please Enter you API key: 
echo:
echo GENAI_APIKEY=%apikey% > .env
echo GENAI_MAX_OUTPUT_TOKENS=300 >> .env
echo GENAI_MODEL=gemini-pro >> .env
echo GENAI_NAME=Gemini >> .env
echo GENAI_TEMPERATURE=0.75 >> .env
echo %tab%%tab% ...Success!\n
timeout /t 1 >NUL


:: Complete installation!
echo ================================================================================================
echo:
echo You have completed the installation of GenAI CLI-tool!
echo:
echo Please use `%cd%\.venv\Scripts\python main.py -m "your-question"` to get a response from GenAI.
echo:
echo Or use `%cd%\.venv\Scripts\python main.py -i` to use the interactive mode."
echo:
echo You can also make an alias in your startup file (e.g. ~/.bashrc) to make it more convenient.
echo:
echo Use `%cd%\.venv\bin\python3 main.py -h ` to get more information.
echo:
echo Have fun!
echo:
echo ================================================================================================
timeout /t -1 >NUL
