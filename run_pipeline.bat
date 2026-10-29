@echo off
title Employee Attendance Analytics Pipeline
echo =====================================================================
echo    Launching Employee Attendance Analytics Master Pipeline...
echo =====================================================================
echo.

set PYTHON_EXE=C:\Users\HP\AppData\Local\Programs\Python\Python314\python.exe

if exist "%PYTHON_EXE%" (
    "%PYTHON_EXE%" main.py
) else (
    python main.py
)

echo.
echo =====================================================================
echo Execution Completed. Press any key to exit...
echo =====================================================================
pause >nul
