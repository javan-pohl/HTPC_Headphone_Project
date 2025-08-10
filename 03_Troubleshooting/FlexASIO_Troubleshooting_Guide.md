# FlexASIO Windows 11 Troubleshooting Guide

## Current Setup Overview
- **Hardware**: HP Envy laptop (Windows 11) → HDMI 2.0 → Anthem AVM70 → Topping L50
- **Audio Pipeline**: Kodi → LAV Filters → FlexASIO → Virtuoso v2 → Anthem DAC
- **Goal**: 7.1.4 Atmos/DTS-HD → PCM → binaural processing
- **Issue**: FlexASIO not appearing as audio device in Kodi

## Diagnostic Steps

### 1. Verify FlexASIO Installation
Run these commands in **Administrator** Command Prompt:

```cmd
# Check if FlexASIO is registered
regsvr32 /s "C:\Program Files\FlexASIO\FlexASIO_x64.dll"

# List registered ASIO drivers
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\ASIO" /s
```

### 2. Check FlexASIO Service Status
```cmd
# Check Windows Audio service
sc query AudioSrv
sc query AudioEndpointBuilder

# Restart audio services if needed
net stop AudioSrv
net stop AudioEndpointBuilder
net start AudioEndpointBuilder
net start AudioSrv
```

### 3. Verify Virtuoso Connection
- Open **Virtuoso v2**
- Check if FlexASIO appears in audio device list
- Confirm layout is set to "Dolby Atmos 7.1.4"

### 4. Test FlexASIO in Different Applications

#### Test with ASIO4ALL Panel (if available):
1. Download and install ASIO4ALL temporarily
2. See if your audio devices appear
3. If yes, FlexASIO should work too

#### Test with REW (Room EQ Wizard):
1. Download REW (free)
2. Set audio driver to FlexASIO
3. Check if device appears and shows 12 channels

## Common Windows 11 Fixes

### Fix 1: Compatibility Mode
1. Navigate to FlexASIO installation folder
2. Right-click `FlexASIO_x64.dll`
3. Properties → Compatibility
4. Check "Run this program in compatibility mode"
5. Select "Windows 10"
6. Apply and restart

### Fix 2: Re-register FlexASIO
```cmd
# Run as Administrator
cd "C:\Program Files\FlexASIO"
regsvr32 /u FlexASIO_x64.dll
regsvr32 FlexASIO_x64.dll
```

### Fix 3: Windows Audio Driver Reset
```cmd
# Reset Windows Audio
sfc /scannow
dism /online /cleanup-image /restorehealth
```

### Fix 4: HDMI Audio Driver Update
1. Device Manager → Sound, video and game controllers
2. Right-click "Intel Display Audio" (or similar)
3. Update driver
4. If Windows doesn't find newer: download Intel Driver & Support Assistant

### Fix 5: FlexASIO Configuration File
Create/edit `FlexASIO.toml` in your user folder or FlexASIO directory:

```toml
backend = "Windows DirectSound"
[input]
device = "YOUR_INPUT_DEVICE_NAME"
[output]
device = "YOUR_OUTPUT_DEVICE_NAME"
channels = 12
sampleType = "Int32"
```

## Kodi-Specific Configuration

### Audio Settings for Kodi:
1. **Settings** → **System** → **Audio**
2. **Audio output device**: FlexASIO
3. **Channels**: 7.1
4. **Output configuration**: Fixed
5. **Enable exclusive mode**: Yes (if available)
6. **Allow passthrough**: No (we want PCM decoding)

### LAV Audio Decoder Settings:
1. Right-click video in Kodi → Audio settings
2. Ensure LAV is set to PCM output
3. Check format support includes Atmos/DTS-HD

## Advanced Troubleshooting

### Check Windows Audio Exclusive Mode:
1. Control Panel → Sound
2. Select your HDMI output device
3. Properties → Advanced
4. Uncheck "Allow applications to take exclusive control"
5. Restart and test

### Alternative: Use External Player
If Kodi internal player fails:
1. Install MPC-HC or MPC-BE
2. Configure as external player in Kodi
3. Set LAV Filters in MPC
4. Configure FlexASIO in MPC

## Verification Tests

### Test 1: Channel Mapping
In Virtuoso:
1. Play test tones for each channel
2. Verify all 12 inputs (7.1.4) are receiving signal
3. Check binaural output is working

### Test 2: Format Support
Test with known Atmos/DTS-HD content:
1. Play sample file
2. Verify decoder shows proper format
3. Check output to Anthem shows PCM 7.1

### Test 3: Latency Check
- Measure audio delay with test tones
- Adjust in Kodi or Virtuoso as needed
- Document delay values for each display (OLED: 10ms, NZ7: 35ms)

## If All Else Fails

### Alternative Solutions:
1. **VoiceMeeter Banana**: Can route audio between applications
2. **VB-Cable**: Virtual audio cable solution
3. **OBS Virtual Audio**: Another routing option
4. **Direct hardware connection**: Bypass PC processing entirely

### Hardware-based Alternative:
- Connect sources directly to Anthem
- Use Anthem's internal processing
- Skip PC-based binaural processing

## Error Tracking

### Common Error Messages:
- "No ASIO driver found"
- "FlexASIO initialization failed"
- "Device already in use"
- "Sample rate not supported"

### Solutions Database:
| Error | Cause | Solution |
|-------|-------|----------|
| No ASIO driver | Not registered | Re-register DLL |
| Init failed | Driver conflict | Restart audio services |
| Device in use | Exclusive mode | Close other apps |
| Sample rate | Mismatch | Set consistent rates |

## Next Steps After Fix

1. **Configure audio delay** for each display
2. **Set up HRIR measurement** workflow with binaural mics
3. **Plan bass shaker integration** via secondary USB interface
4. **Document working configuration** for future reference 