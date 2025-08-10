@echo off
echo ========================================
echo FlexASIO Registration Status Check
echo ========================================
echo.

echo [1] Checking ASIO registry entries...
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO" >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✓ ASIO registry key exists
    echo.
    echo    ASIO drivers found:
    for /f "skip=1 tokens=*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO" 2^>nul') do (
        echo    - %%a
    )
) else (
    echo    ✗ No ASIO registry entries found
)

echo.
echo [2] Checking WOW6432Node (32-bit) ASIO entries...
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\ASIO" >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✓ 32-bit ASIO registry key exists
    echo.
    echo    32-bit ASIO drivers found:
    for /f "skip=1 tokens=*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\ASIO" 2^>nul') do (
        echo    - %%a
    )
) else (
    echo    ✗ No 32-bit ASIO registry entries found
)

echo.
echo [3] Specific FlexASIO registration check...
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO\FlexASIO" >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✓ FlexASIO (64-bit) registered
) else (
    echo    ✗ FlexASIO (64-bit) NOT registered
)

reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\ASIO\FlexASIO" >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✓ FlexASIO (32-bit) registered
) else (
    echo    ✗ FlexASIO (32-bit) NOT registered
)

echo.
echo [4] File existence check...
if exist "C:\Program Files\FlexASIO\x64\FlexASIO.dll" (
    echo    ✓ FlexASIO x64 DLL exists
) else (
    echo    ✗ FlexASIO x64 DLL missing
)

if exist "C:\Program Files\FlexASIO\x86\FlexASIO.dll" (
    echo    ✓ FlexASIO x86 DLL exists
) else (
    echo    ✗ FlexASIO x86 DLL missing
)

echo.
echo ========================================
echo Summary:
echo - If both 64-bit AND 32-bit show as registered,
echo   FlexASIO should appear in most applications
echo - If only 64-bit is registered, only 64-bit apps
echo   (like REW) will see FlexASIO
echo - Media players often need 32-bit registration
echo ========================================
pause