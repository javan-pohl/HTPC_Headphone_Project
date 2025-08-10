# VoiceMeeter Banana Installation & Configuration Guide

## 🎯 **Goal**
Set up VoiceMeeter Banana to route Kodi audio → FlexASIO → HeSuVi for high-channel Atmos binaural processing (7.1.6+/9.2.6+)

## 📥 **Step 1: Download VoiceMeeter Banana**

1. **Visit**: https://voicemeeter.com/
2. **Navigate to**: "Download" section
3. **Select**: "VoiceMeeter Banana" (the middle option)
   - **Standard VoiceMeeter**: 2 inputs, 2 outputs (insufficient)
   - **VoiceMeeter Banana**: 3 inputs, 5 outputs ✓ (recommended for our use)
   - **VoiceMeeter Potato**: 5 inputs, 8 outputs (overkill but also works)
4. **Download**: VoiceMeeterSetup.exe

## ⚙️ **Step 2: Install VoiceMeeter Banana**

1. **Right-click** VoiceMeeterSetup.exe → **"Run as administrator"**
2. **Follow installer**: Accept license, default installation path
3. **Important**: Installer will prompt for **REBOOT** - this is required!
4. **Reboot** your computer (virtual audio drivers need to be loaded)

## 🔧 **Step 3: Initial VoiceMeeter Configuration**

### Launch VoiceMeeter Banana
1. **Start Menu** → Search "VoiceMeeter" → Launch "VoiceMeeter Banana"
2. **If prompted**: Allow Windows Defender/Firewall access

### Basic Hardware Setup
1. **A1 Output** (top right):
   - Click on "A1" dropdown
   - Select your **default Windows audio device** (e.g., "Speakers", "Headphones")
   - This ensures you can still hear system sounds

2. **A2 Output** (ASIO - this is key!):
   - Click on "A2" dropdown  
   - Select **"ASIO Driver"**
   - Click **"SELECT"** button next to A2
   - **Choose "FlexASIO"** from the ASIO driver list
   - **Set Sample Rate**: 48000 Hz (match FlexASIO config)
   - **Set Buffer**: 512 samples (match FlexASIO config)

### Virtual Input Configuration  
1. **VAIO** (Virtual Audio Input - left side):
   - This is where Kodi will send audio
   - **A1 button**: Click to enable (routes to your speakers/headphones)
   - **A2 button**: Click to enable (routes to FlexASIO ASIO)
   - Both should be **GREEN/LIT** when enabled

## 🎵 **Step 4: Configure Kodi for VoiceMeeter**

1. **Open Kodi**
2. **Navigate**: Settings → System → Audio
3. **Audio output device**: 
   - Look for **"VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)"**
   - Select this option
4. **Number of channels**: **7.1** or higher (for high-channel Atmos content - 7.1.6+/9.2.6+)
5. **Output configuration**: **Fixed**
6. **Allow passthrough**: **Disabled** (we want PCM decoding)
7. **Keep audio device alive**: **Always** (recommended)

## 🧪 **Step 5: Test Audio Flow**

### Basic Test
1. **Play any audio** in Kodi (music, video, anything)
2. **Watch VoiceMeeter**: 
   - **VAIO input** should show **green level meters** moving
   - **A1 output** should have audio (you hear it normally)
   - **A2 output** should be routing to FlexASIO

### Verify FlexASIO Receives Audio
1. **Open REW** (Room EQ Wizard)
2. **Preferences** → **Soundcard**
3. **Audio Device**: ASIO
4. **ASIO Device**: FlexASIO
5. **Check**: Input level meters should show activity when Kodi plays

## 🔧 **Step 6: Troubleshooting Common Issues**

### No Audio in VoiceMeeter
- **Check**: Kodi audio output device selection
- **Verify**: VoiceMeeter VAIO is selected in Kodi
- **Restart**: Both Kodi and VoiceMeeter

### No Audio to FlexASIO (A2)
- **Check**: A2 is set to "ASIO Driver" 
- **Verify**: FlexASIO is selected in A2 ASIO settings
- **Enable**: A2 button on VAIO input (should be green)
- **Match**: Sample rates between VoiceMeeter and FlexASIO (48kHz)

### Audio Quality Issues
- **Buffer size**: Try 256, 512, or 1024 samples
- **Sample rate**: Ensure 48000 Hz throughout chain
- **Exclusive mode**: Disable WASAPI exclusive in FlexASIO.toml

### Can't Select FlexASIO in A2
- **Restart**: VoiceMeeter as Administrator
- **Check**: FlexASIO registration (run our registration scripts)
- **Verify**: FlexASIO appears in REW first

## 📊 **Step 7: Success Verification**

### ✅ Checklist:
- [ ] VoiceMeeter shows VAIO input levels when Kodi plays
- [ ] Can hear audio normally through A1 (speakers/headphones)  
- [ ] REW shows FlexASIO receiving audio signal from A2
- [ ] No audio dropouts or distortion
- [ ] 7.1 content properly routed (verify in channel meters)

### Next Steps After Success:
1. **Download HeSuVi** for binaural processing
2. **Configure HeSuVi** to use FlexASIO as input
3. **Test complete pipeline**: Kodi → VoiceMeeter → FlexASIO → HeSuVi → Headphones

## 💡 **Pro Tips**

- **Save configuration**: VoiceMeeter → Menu → Save Settings
- **Auto-start**: VoiceMeeter can auto-launch with Windows
- **Monitoring**: Use A3 output for monitoring/recording if needed
- **Latency**: Lower buffer sizes = lower latency but higher CPU usage
- **Multiple outputs**: Can route to both speakers (A1) and ASIO (A2) simultaneously

---

**Ready to download and install VoiceMeeter Banana?**