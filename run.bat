@echo off
echo ========================================================
echo   Starting Shaurya's Personal Portfolio (Flask Web App)
echo   Python Lab Experiment No. 12
echo ========================================================
echo.

:: Check if virtual environment exists, if not create it
if not exist "venv" (
    echo [1/3] Creating virtual environment 'venv'...
    python -m venv venv
    echo.
)

:: Activate virtual environment
echo [2/3] Activating virtual environment...
call venv\Scripts\activate.bat

:: Install required packages
echo [3/3] Installing dependencies from requirements.txt...
pip install -r requirements.txt --quiet
echo.

echo ========================================================
echo   Application is ready! Starting Flask server...
echo   Open your browser at: http://127.0.0.1:5000
echo   Press CTRL+C in this terminal to stop the server.
echo ========================================================
echo.

python app.py

pause
