@echo off
setlocal

REM Determine repository base folder (normalized)
for %%I in ("%~dp0.") do set "PROJECT_DIR=%%~fI"
set "VENV_DIR=%PROJECT_DIR%\.venv"
set "LAUNCHER_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps"
set "LAUNCHER_FILE=%LAUNCHER_DIR%\assistant.cmd"

REM Remove the virtual environment folder if it exists
if exist "%VENV_DIR%" (
    rmdir /s /q "%VENV_DIR%"
)

REM Delete persisted data file if you want a clean slate
if exist "%PROJECT_DIR%\books.pkl" (
    del /q "%PROJECT_DIR%\books.pkl"
)

REM Remove global launcher command
if exist "%LAUNCHER_FILE%" (
    del /q "%LAUNCHER_FILE%"
)

echo Cleanup complete. Press any key to close...
pause

endlocal
