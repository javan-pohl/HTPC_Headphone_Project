@echo off
echo ========================================
echo Manual FlexASIO Cleanup Script
echo ========================================
echo This will completely remove FlexASIO remnants
echo Run as Administrator only!
echo.
pause

echo.
echo [1] Stopping audio services...
net stop AudioSrv
net stop AudioEndpointBuilder

echo.
echo [2] Attempting to unregister DLLs (may fail)...
cd "C:\Program Files\FlexASIO\x64" 2>nul
regsvr32 /u /s FlexASIO.dll 2>nul
cd "C:\Program Files\FlexASIO\x86" 2>nul  
regsvr32 /u /s FlexASIO.dll 2>nul

echo.
echo [3] Removing FlexASIO directory...
rd /s /q "C:\Program Files\FlexASIO" 2>nul
if exist "C:\Program Files\FlexASIO" (
    echo    Warning: Some files may still exist
    attrib -r -h -s "C:\Program Files\FlexASIO\*.*" /s /d 2>nul
    rd /s /q "C:\Program Files\FlexASIO" 2>nul
)

echo.
echo [4] Cleaning registry entries...
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO\FlexASIO" /f 2>nul
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\ASIO\FlexASIO" /f 2>nul

echo.
echo [5] Removing from Programs list...
REM Find and remove FlexASIO entries from uninstall registry
for /f "tokens=*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" /s /k /f "FlexASIO" 2^>nul ^| findstr /c:"HKEY_"') do (
    echo Removing registry key: %%a
    reg delete "%%a" /f 2>nul
)

for /f "tokens=*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall" /s /k /f "FlexASIO" 2^>nul ^| findstr /c:"HKEY_"') do (
    echo Removing registry key: %%a
    reg delete "%%a" /f 2>nul
)

echo.
echo [6] Restarting audio services...
net start AudioEndpointBuilder
net start AudioSrv

echo.
echo [7] Cleaning temp files...
del /f /q "%TEMP%\FlexASIO*" 2>nul
del /f /q "%LOCALAPPDATA%\Temp\FlexASIO*" 2>nul

echo.
echo ========================================
echo Cleanup Complete!
echo.
echo Next steps:
echo 1. Check Add/Remove Programs - FlexASIO should be gone
echo 2. Reboot your computer
echo 3. Download fresh FlexASIO installer
echo 4. Install as Administrator
echo ========================================
pause 