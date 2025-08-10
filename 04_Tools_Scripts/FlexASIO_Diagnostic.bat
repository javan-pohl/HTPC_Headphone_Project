@echo off
echo ========================================
echo FlexASIO Diagnostic Script
echo ========================================
echo.

echo Checking FlexASIO installation...
echo.

REM Check if FlexASIO files exist
echo [1] Checking FlexASIO files:
if exist "C:\Program Files\FlexASIO\x64\FlexASIO.dll" (
    echo    ✓ FlexASIO.dll (x64) found
) else (
    echo    ✗ FlexASIO.dll (x64) MISSING
)

if exist "C:\Program Files\FlexASIO\x86\FlexASIO.dll" (
    echo    ✓ FlexASIO.dll (x86) found
) else (
    echo    ✗ FlexASIO.dll (x86) MISSING
)
echo.

REM Check registry entries
echo [2] Checking ASIO registry entries:
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO" >nul 2>&1
if %errorlevel% == 0 (
    echo    ✓ ASIO registry key exists
    reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO\FlexASIO" >nul 2>&1
    if %errorlevel% == 0 (
        echo    ✓ FlexASIO registered in ASIO
    ) else (
        echo    ✗ FlexASIO NOT registered in ASIO
    )
) else (
    echo    ✗ No ASIO registry entries found
)
echo.

REM Check Windows Audio services
echo [3] Checking Windows Audio services:
sc query AudioSrv | find "RUNNING" >nul
if %errorlevel% == 0 (
    echo    ✓ Windows Audio Service running
) else (
    echo    ✗ Windows Audio Service not running
)

sc query AudioEndpointBuilder | find "RUNNING" >nul
if %errorlevel% == 0 (
    echo    ✓ Audio Endpoint Builder running
) else (
    echo    ✗ Audio Endpoint Builder not running
)
echo.

REM List audio devices
echo [4] Available audio devices:
powershell -Command "Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status" 2>nul
echo.

REM Check HDMI audio specifically
echo [5] HDMI Audio devices:
powershell -Command "Get-WmiObject -Class Win32_SoundDevice | Where-Object {$_.Name -like '*HDMI*' -or $_.Name -like '*Display*'} | Select-Object Name, Status" 2>nul
echo.

echo ========================================
echo Recommendations:
echo.
if not exist "C:\Program Files\FlexASIO\x64\FlexASIO.dll" (
    echo - Reinstall FlexASIO with Administrator privileges
)
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO\FlexASIO" >nul 2>&1
if %errorlevel% neq 0 (
    echo - Register FlexASIO: Run Register_FlexASIO.bat as Administrator
)
echo - Test in Virtuoso to see if FlexASIO appears
echo - Check Kodi audio settings for FlexASIO option
echo.
echo ========================================
pause 