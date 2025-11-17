@echo off
REM Launch assistant bot from any terminal using the prepared virtual environment
for %%I in ("%~dp0.") do set "ROOT=%%~fI"
pushd "%ROOT%"

if not exist ".venv\Scripts\activate.bat" (
    echo Virtual environment is missing. Run the installer first.
    popd
    exit /b 1
)

call ".venv\Scripts\activate.bat"
python main.py %*
deactivate

popd
