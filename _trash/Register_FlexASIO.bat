@echo off
echo ========================================
echo FlexASIO Registration Script
echo ========================================
echo This will register FlexASIO as an ASIO driver
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

echo Checking if FlexASIO files exist...
if not exist "C:\Program Files\FlexASIO\x64\FlexASIO.dll" (
    echo ERROR: FlexASIO x64 DLL not found!
    echo Please reinstall FlexASIO first.
    pause
    exit /b 1
)

if not exist "C:\Program Files\FlexASIO\x86\FlexASIO.dll" (
    echo ERROR: FlexASIO x86 DLL not found!
    echo Please reinstall FlexASIO first.
    pause
    exit /b 1
)

echo.
echo [1] Registering 64-bit FlexASIO...
regsvr32 "C:\Program Files\FlexASIO\x64\FlexASIO.dll"
if %errorlevel% equ 0 (
    echo    ✓ 64-bit FlexASIO registered successfully
) else (
    echo    ✗ Failed to register 64-bit FlexASIO
)

echo.
echo [2] Registering 32-bit FlexASIO...
regsvr32 "C:\Program Files\FlexASIO\x86\FlexASIO.dll"
if %errorlevel% equ 0 (
    echo    ✓ 32-bit FlexASIO registered successfully
) else (
    echo    ✗ Failed to register 32-bit FlexASIO
)

echo.
echo [3] Verifying registration...
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO" >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✓ ASIO registry key exists
    reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO\FlexASIO" >nul 2>&1
    if %errorlevel% equ 0 (
        echo    ✓ FlexASIO is properly registered
    ) else (
        echo    ✗ FlexASIO registration not found in registry
    )
) else (
    echo    ✗ No ASIO registry entries found
)

echo.
echo ========================================
echo Registration Complete!
echo.
echo Next steps:
echo 1. Open APL Virtuoso v2
echo 2. Check if FlexASIO appears in audio device list
echo 3. If yes, configure Kodi to use FlexASIO
echo ========================================
pause