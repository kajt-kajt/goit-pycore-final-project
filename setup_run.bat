@echo off
setlocal

REM Normalize project path
for %%I in ("%~dp0.") do set "PROJECT_DIR=%%~fI"
set "VENV_DIR=%PROJECT_DIR%\.venv"

REM Create virtual environment if needed
if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    py -3 -m venv "%VENV_DIR%" || goto ERROR
)

REM Install dependencies inside the environment
call "%VENV_DIR%\Scripts\activate.bat" || goto ERROR
python -m pip install --upgrade pip || goto ERROR
python -m pip install -r "%PROJECT_DIR%\requirements.txt" || goto ERROR
call deactivate

REM Create global launcher in WindowsApps so "assistant" works everywhere
set "LAUNCHER_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps"
set "LAUNCHER_FILE=%LAUNCHER_DIR%\assistant.cmd"
(
    echo @echo off
    echo call "%PROJECT_DIR%\assistant.bat" %%*
)>"%LAUNCHER_FILE%"

echo Setup complete. Open a new CMD/PowerShell window and run: assistant
pause
goto :EOF

:ERROR
echo.
echo Setup failed. Press any key to close...
pause

endlocal
