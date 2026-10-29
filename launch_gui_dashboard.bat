@echo off
title Employee Attendance Interactive GUI Dashboard
echo =====================================================================
echo    Launching Interactive Tkinter Desktop Analytics Dashboard...
echo =====================================================================
echo.

set PYTHON_EXE=C:\Users\HP\AppData\Local\Programs\Python\Python314\python.exe

if exist "%PYTHON_EXE%" (
    "%PYTHON_EXE%" main.py --gui
) else (
    python main.py --gui
)

echo.
pause
