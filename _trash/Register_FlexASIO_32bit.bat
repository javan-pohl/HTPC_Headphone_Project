@echo off
echo ========================================
echo FlexASIO 32-bit Registration Script
echo ========================================
echo This will register the 32-bit FlexASIO driver
echo Run as Administrator ONLY!
echo.

REM Check if running as Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: This script must be run as Administrator!
    echo Right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo Registering 32-bit FlexASIO...
regsvr32 "C:\Program Files\FlexASIO\x86\FlexASIO.dll"

if %errorlevel% equ 0 (
    echo.
    echo ✓ SUCCESS: 32-bit FlexASIO registered successfully
    echo.
    echo Now test in Kodi and MPC-BE - FlexASIO should appear!
) else (
    echo.
    echo ✗ FAILED: 32-bit FlexASIO registration failed
    echo Error code: %errorlevel%
)

echo.
echo ========================================
pause