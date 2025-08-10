# Kodi HTPC Optimal Settings Configuration

**Date**: January 2025  
**System**: Windows 11 HTPC  
**Purpose**: Smooth 4K/HDR playback with 5.1.2 Atmos audio routing through VoiceMeeter  
**Status**: ✅ **TESTED AND WORKING**

## 🎥 **VIDEO SETTINGS**

### **System → Display**
- **Resolution**: Native display resolution (match your monitor/TV)
- **Refresh rate**: **60.03 Hz** (Windows setting - working configuration)
- **Use fullscreen window**: ON
- **Adjust display refresh rate**: **"On start/stop"**
- **Sync playback to display**: ✅ **ON**

### **System → Display → Video Rendering**
- **Video renderer**: ✅ **"Madshi Video Renderer (madVR)"**
- **Direct3D presentation**: ✅ **"Direct3D 11"** (CRITICAL - fixes frame skipping)
  - ❌ **NOT** "Direct3D (no vsync)" - causes stuttering

### **Player → Videos**
- **Adjust display refresh rate**: ✅ **"On start/stop"**
- **Sync playback to display**: ✅ **ON**
- **Allow hardware acceleration**: ✅ **ON**

## 🎧 **AUDIO SETTINGS (5.1.2 ATMOS SETUP)**

### **System → Audio**
- **Audio output device**: ✅ **"VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)"**
- **Number of channels**: ✅ **7.1** (enables 8-channel 5.1.2 output)
- **Output configuration**: ✅ **"Best match"**
- **Maintain original volume on downmix**: ON
- **Allow passthrough**: ✅ **OFF** (we want PCM decode for VoiceMeeter)
- **Boost volume of dialog**: 0 dB (VoiceMeeter handles center channel mixing)

### **Advanced Audio Settings**
- **Audio output device**: VoiceMeeter Input
- **Output configuration**: Fixed
- **Limit sampling rate**: OFF (allow 48kHz for Atmos)
- **Stereo upmix**: OFF (we want discrete channels)
- **Normalize levels on downmix**: ON

## 🔧 **PERFORMANCE OPTIMIZATION**

### **System → Display → Advanced**
- **Use limited color range**: Match your display capability
- **Pixel shaders**: Allow (for madVR processing)

### **Player → Videos → Processing**
- **Allow hardware acceleration**: ✅ **ON**
- **Enable HiQ scalers for software upscaling**: OFF (madVR handles this)
- **Process Info**: Enable (for debugging if needed)

### **System → Audio → Advanced**
- **Audio buffer**: Auto (let system optimize)
- **Audio latency**: Auto
- **Stream silence**: 1 second

## 🖥️ **WINDOWS SYSTEM CONFIGURATION**

### **Windows Display Settings**
- **Refresh rate**: ✅ **60.03 Hz** (working configuration)
- **Resolution**: Native (4K recommended)
- **HDR**: Enable if display supports it

### **Windows Audio Settings**
- **Default playback device**: ✅ **"VoiceMeeter Input"**
- **Spatial sound**: OFF (we handle spatialization through our pipeline)
- **Exclusive mode**: Available for VoiceMeeter if needed

## 📊 **VERIFICATION TESTS**

### **Video Playback Test**
- ✅ **4K UHD content**: No frame skipping or stuttering
- ✅ **24fps content**: Smooth playback with refresh rate switching
- ✅ **HDR content**: Proper tone mapping through madVR

### **Audio Test**
- ✅ **Stereo content**: Clear audio through VoiceMeeter
- ✅ **5.1 content**: All channels active, center mixed to stereo for monitoring
- ✅ **Atmos content**: 8 channels active in VoiceMeeter (press Ctrl+Shift+O in Kodi, should show "PCM 8-ch @48 kHz")

### **Debug Verification**
1. **Play Atmos content**
2. **Press Ctrl + Shift + O** to show codec info
3. **Should display**: "PCM 8-ch @48 kHz"
4. **VoiceMeeter**: All 8 level meters showing activity
5. **Audio**: Center channel audible with "Mix Down A" enabled

## 🎯 **CRITICAL SUCCESS FACTORS**

### **What Fixed Frame Skipping:**
1. ✅ **Direct3D 11 presentation** (instead of "no vsync")
2. ✅ **madVR renderer** (superior to other options)
3. ✅ **Sync playback to display** enabled
4. ✅ **Refresh rate switching** on start/stop

### **What Enables 5.1.2 Atmos:**
1. ✅ **7.1 channel setting** in Kodi
2. ✅ **Passthrough OFF** (PCM decode required)
3. ✅ **VoiceMeeter Input** as audio device
4. ✅ **VoiceMeeter A1 mixdown** for stereo monitoring

## 🔄 **PIPELINE STATUS**

### **Currently Working:**
```
Kodi (8-ch PCM) → VoiceMeeter Banana → 
├── A1 Output (stereo with mixdown) → DAC/Speakers ✅
└── Insert ASIO (8-ch discrete) → [Ready for Virtuoso]
```

### **Next Steps:**
- [ ] Verify VoiceMeeter Insert Virtual ASIO driver availability
- [ ] Install and configure APL Virtuoso v2 for binaural processing
- [ ] Test complete 5.1.2 → binaural → headphones pipeline

## 🛠️ **TROUBLESHOOTING NOTES**

### **If Video Stutters:**
1. **Check Direct3D presentation**: Must be "Direct3D 11"
2. **Verify madVR renderer**: Should not be using basic renderers
3. **Display sync**: Ensure "Sync playback to display" is ON

### **If Audio Issues:**
1. **Check VoiceMeeter meters**: All 8 should show activity for Atmos
2. **Center channel**: Enable "Mix Down A" in VoiceMeeter A1 bus
3. **Debug overlay**: Ctrl+Shift+O should show "PCM 8-ch"

### **If Performance Issues:**
1. **Hardware acceleration**: Verify it's enabled and working
2. **madVR settings**: Check for excessive processing options
3. **System resources**: Monitor CPU/GPU usage during playback

---

**Configuration Status**: ✅ **STABLE AND WORKING**  
**Last Updated**: January 2025  
**Ready for**: Virtuoso v2 binaural processing integration
