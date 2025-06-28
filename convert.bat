@echo off
REM Convenience batch file to run the Image to PDF Converter
REM Uses the correct Python installation where packages are installed

set PYTHON_EXE=C:\Users\kalin\AppData\Local\Programs\Python\Python313\python.exe

if "%1"=="" (
    echo Usage: convert.bat [script] [arguments]
    echo.
    echo Examples:
    echo   convert.bat image_to_pdf_converter.py --help
    echo   convert.bat image_to_pdf_converter.py image.jpg
    echo   convert.bat gui_converter.py
    echo   convert.bat test_converter.py
    echo.
    goto :eof
)

%PYTHON_EXE% %* 