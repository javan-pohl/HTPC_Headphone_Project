# FlexASIO Fix - Missing DLL Files

## Problem Identified
**FlexASIO installation is incomplete** - the DLL files are missing from both x64 and x86 directories.

## Immediate Solution

### Step 1: Download Fresh FlexASIO
1. Go to https://github.com/dechamps/FlexASIO/releases
2. Download the latest **FlexASIO-1.10b.exe** (current latest version)
3. **Important**: Download directly, don't use any package manager

### Step 2: Completely Remove Current Installation
```cmd
# Run as Administrator in Command Prompt (not WSL)
cd "C:\Program Files\FlexASIO"
regsvr32 /u x64\FlexASIO_x64.dll  # May fail since file missing
regsvr32 /u x86\FlexASIO_x86.dll  # May fail since file missing

# Remove the directory
rd /s /q "C:\Program Files\FlexASIO"
```

### Step 3: Clean Registry
```cmd
# Remove any registry entries
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO\FlexASIO" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\ASIO\FlexASIO" /f
```

### Step 4: Fresh Installation
1. **Right-click** FlexASIO installer → **Run as Administrator**
2. Choose **Custom Installation**
3. Ensure both x86 and x64 options are checked
4. Install to default location: `C:\Program Files\FlexASIO`

### Step 5: Verify Installation
After installation, check these files exist:
- `C:\Program Files\FlexASIO\x64\FlexASIO.dll`
- `C:\Program Files\FlexASIO\x86\FlexASIO.dll`

### Step 6: Manual Registration (if needed)
```cmd
# Run as Administrator
cd "C:\Program Files\FlexASIO\x64"
regsvr32 FlexASIO.dll

# Should see "DllRegisterServer in FlexASIO.dll succeeded"
```

### Step 7: Test with Virtuoso
1. Open **APL Virtuoso v2**
2. Check audio device dropdown
3. **FlexASIO** should now appear
4. Select it and verify 7.1.4 layout is detected

## Alternative: Use KoordASIO Instead

If FlexASIO continues to have issues, try **KoordASIO** (FlexASIO fork with GUI):

1. Download from: https://github.com/koord-live/KoordASIO/releases
2. Install KoordASIO
3. It includes a **Control Panel GUI** for easier configuration
4. Should work identically to FlexASIO but with better Windows 11 compatibility

## Kodi Configuration After Fix

Once FlexASIO is working:

### Audio Settings:
1. **Settings** → **System** → **Audio**
2. **Audio output device**: Select **FlexASIO**
3. **Number of channels**: **7.1**
4. **Output configuration**: **Fixed**
5. **Allow passthrough**: **Disabled** (we want PCM decoding)

### LAV Audio Decoder:
1. Install/configure LAV Filters if not done
2. Set to decode to PCM (not bitstream)
3. Ensure Atmos/DTS-HD support is enabled

## Testing the Complete Chain

### Test 1: Basic Connectivity
1. Play any audio in Kodi
2. Check if Virtuoso shows input signal
3. Verify binaural output to Anthem

### Test 2: Multichannel Test
1. Use Atmos test file
2. Verify all 12 channels (7.1.4) show activity in Virtuoso
3. Check proper binaural rendering

### Test 3: Format Verification
- Play DTS-HD MA 7.1 content
- Verify LAV decodes to PCM
- Confirm Anthem receives proper signal

## If Installation Still Fails

### Check Windows Defender/Antivirus
- FlexASIO DLLs might be quarantined
- Add FlexASIO folder to exclusions
- Restore any quarantined files

### Try Alternative Download Source
- Microsoft Store version (if available)
- Chocolatey: `choco install flexasio`
- Direct GitHub release download

### Compatibility Mode
If installer fails:
1. Right-click installer
2. Properties → Compatibility
3. "Run in compatibility mode for Windows 10"
4. "Run as administrator"

## Next Steps After Fix
1. Configure audio delays (10ms OLED, 35ms NZ7)
2. Test with various content types
3. Document working configuration
4. Prepare for HRIR measurement workflow 