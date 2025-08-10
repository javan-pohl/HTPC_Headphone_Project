# Topping D90 III Sabre USB Driver Setup Guide

## Why You Need the Proper Driver

### Current Situation (Generic Windows Driver)
- Device shows as "Speakers D90 III Sabre"
- Limited sample rate options (up to 384kHz max)
- Uses Windows shared audio mode
- No WASAPI Exclusive or ASIO options available
- Potential for higher USB latency and driver issues

### With Proper Topping XMOS Driver
- Device shows as "Topping D90" or similar
- Full sample rate support up to **768kHz PCM** and **DSD512**
- **WASAPI Exclusive mode** available (bypasses Windows audio stack)
- **ASIO driver** support for professional audio software
- Optimized USB communication and buffer management
- **May resolve static/noise issues** through better driver implementation

## Sample Rate Capabilities Unlocked

| Format | Maximum Support |
|--------|----------------|
| PCM | 32-bit/768kHz |
| DSD | DSD512 (22.5MHz) |
| Native DSD | Yes (if source supports it) |

## Installation Steps

### Step 1: Download the Driver
1. Go directly to the **D90 III Sabre product page**: https://www.toppingaudio.com/product-item/d90-iii-sabre
2. Scroll down to the **"Downloads"** section (below product specifications)
3. Look for **"V5.72 driver for most of TOPPING DACs"** link
4. Click to download the driver installer (typically 10-20MB .exe file)

### Step 2: Uninstall Generic Driver (Recommended)
1. Open **Device Manager** (Right-click Start → Device Manager)
2. Expand **Sound, video and game controllers**
3. Right-click on "Speakers D90 III Sabre" or similar
4. Select **Uninstall device**
5. Check "Delete the driver software for this device" if available
6. Click **Uninstall**

### Step 3: Install Topping Driver
1. **Disconnect the D90** from USB temporarily
2. Run the downloaded Topping driver installer as **Administrator**
3. Follow installation prompts
4. **Restart your computer** when installation completes
5. **Reconnect the D90** via USB

### Step 4: Verify Installation
1. Open **Settings** → **System** → **Sound**
2. Check that device name has changed (may show as "Topping D90" or "XMOS USB Audio")
3. Click on the device → **Device properties** → **Additional device properties**
4. Go to **Advanced** tab
5. **Verify**: Sample rate dropdown should now include options up to **32 bit, 768000 Hz (Studio Quality)**

## Configuration Recommendations

### Windows Audio Settings
- **Default format**: 24-bit, 96kHz or 192kHz for general use
- **Exclusive mode**: Check "Allow applications to take exclusive control"
- **Signal enhancements**: Disable all enhancements and spatial audio

### For Different Use Cases

#### Spotify/Streaming (320kbps max)
- **Recommended**: 24-bit, 48kHz or 96kHz
- **Why**: Higher rates provide no benefit for compressed audio

#### High-Resolution Files
- **Recommended**: Match source sample rate (e.g., 24/192 file → 192kHz output)
- **Avoid**: Unnecessary upsampling

#### DSD Files
- **Recommended**: Native DSD mode if your player supports it
- **Alternative**: DSD to PCM conversion at 176.4kHz or 352.8kHz

#### Maximum Quality Test
- **Format**: 32-bit, 768kHz (for testing only)
- **Note**: Only useful for specific high-resolution content or testing

## Audio Software Configuration

### Foobar2000
1. Go to **Preferences** → **Playback** → **Output**
2. Select **WASAPI (event)**: Topping D90
3. Check **Exclusive mode**
4. Set buffer length to 500-1000ms

### VLC Media Player
1. **Tools** → **Preferences** → **Audio**
2. Output module: **Windows Audio Session API**
3. Device: Select Topping D90
4. Check **Use S/PDIF when available** if desired

### AIMP
1. **Preferences** → **Audio** → **Audio System**
2. Select **WASAPI** output
3. Choose Topping D90 device
4. Enable **Exclusive mode**

### Professional Software (Reaper, etc.)
- ASIO driver should now be available as "Topping USB Audio ASIO"
- Buffer size: Start with 512 samples, adjust as needed

## Troubleshooting

### Driver Not Installing
- **Must run installer as Administrator** (common cause of failure)
- Temporarily disable antivirus during installation
- Ensure D90 is disconnected during installation

### No High Sample Rates Showing / Still Limited to 384kHz
- **USB 2.0 bandwidth limitation**: 384kHz max suggests USB 2.0 port/cable
- Try **USB 3.0 port** (usually blue) with USB 3.0 certified cable
- Restart Windows after driver installation and reconnect D90
- Check if firmware update is available for D90
- **Note**: 384kHz is adequate for audio quality; 768kHz mainly for future-proofing

### Device Not Recognized
- Try different USB cable (USB 2.0 certified minimum)
- Check Windows Update for additional driver components
- Reinstall driver if necessary

### Static/Noise After Driver Installation
- Driver installation may help but **static issues are typically hardware/electrical**
- Increase buffer size in audio software
- Use WASAPI Exclusive mode
- **Primary solution**: USB isolator (HS02) for electrical noise issues

## Expected Benefits

### Audio Quality
- **Bit-perfect playback** with WASAPI Exclusive
- **Lower latency** with optimized ASIO driver
- **Better timing** and reduced jitter

### Noise Reduction
- **Improved USB communication** may reduce electrical noise
- **Bypass Windows audio stack** eliminates software interference
- **Optimized buffer management** reduces dropouts and glitches
- **Note**: For persistent static, hardware solutions (USB isolator) typically required

### Future-Proofing
- **Full format support** for any high-resolution content
- **Native DSD** playback capability
- **Professional software compatibility**

## Sample Rate Practical Guide

| Content Type | Recommended Setting | Why |
|-------------|-------------------|-----|
| Spotify, YouTube Music | 48kHz | Matches streaming quality |
| CD rips (44.1kHz) | 44.1kHz or 88.2kHz | Avoids resampling |
| High-res downloads | Match source | Preserves original quality |
| DSD files | Native DSD or 176.4kHz | Optimal DSD handling |
| General listening | 96kHz | Good balance of quality/compatibility |

---
*Document created: [Current Date]*  
*Last updated: [Current Date]*
