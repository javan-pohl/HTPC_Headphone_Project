# Kodi 5.1.2 Atmos to Headphone Virtualization Guide

**Date**: January 2025  
**Goal**: Extract 5.1.2 PCM from Kodi and process through binaural virtualization for headphones

## 🎯 **PROJECT OVERVIEW**

This guide demonstrates how to extract 5.1.2 (8-channel) Dolby Atmos content from Kodi and route it through binaural processing for headphone playback. While this approach is limited to 8 channels maximum (not full 16+ channel Atmos), it provides a viable solution for overhead audio effects through headphones.

## 📊 **TECHNICAL FOUNDATION**

### Kodi's Atmos Decoding Capability
- **What Kodi Can Do**: Decode Atmos content to 8-channel PCM (5.1.2 layout)
- **Channel Mapping**: L, R, C, LFE, Ls, Rs, Top Front L, Top Front R
- **Height Limitation**: Only first two height objects; additional objects folded into base 7.1 bed
- **Decoder**: Uses LAV Filters/FFmpeg - same limitation across all mainstream Windows media players

### Channel Layout Explanation
```
5.1.2 Layout (8 channels total):
Front:  L  C  R
Sides:    Ls Rs
LFE:       •
Height:  TFL TFR (Top Front Left/Right)
```

## 🔧 **COMPLETE AUDIO PIPELINE**

```
Kodi (Atmos decode → 8-ch PCM 5.1.2)
  ↓ WASAPI
VoiceMeeter VAIO (7.1 device capture)
  ↓ VoiceMeeter INSERT ASIO (32-ch bridge)
FlexASIO (24-ch universal ASIO driver)
  ↓ 
Binaural Processor:
  A) HeSuVi (free, limited height awareness)
  B) APL Virtuoso v2 (professional, full height support)
  ↓
Headphones
```

## 📋 **STEP-BY-STEP SETUP GUIDE**

### Prerequisites
- Windows 10/11
- Kodi v20+ (contains FFmpeg 5+ with Atmos support)
- VoiceMeeter Banana 3.0.2.4+
- FlexASIO 1.11+ (installed & registered)
- Binaural processor: HeSuVi (free) or APL Virtuoso v2 (trial/paid)
- Quality headphones with DAC/amplifier

### Step 1: Configure Kodi for 5.1.2 Output

**Kodi Audio Settings:**
1. Settings → System → Audio
2. **Audio output device**: "VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)"
3. **Number of channels**: 7.1 (this enables 8-channel output)
4. **Output configuration**: Best match
5. **Allow passthrough**: OFF (we want decoded PCM, not bitstream)

**Verification:**
- Play Atmos content
- Press Ctrl + Shift + O to show debug info
- Should display: "PCM 8-ch @48 kHz"

**Result Channel Mapping:**
- Ch1: L (Left)
- Ch2: R (Right) 
- Ch3: C (Center)
- Ch4: LFE (Low Frequency Effects)
- Ch5: Ls (Left Surround)
- Ch6: Rs (Right Surround)
- Ch7: TFL (Top Front Left) ← Height channel
- Ch8: TFR (Top Front Right) ← Height channel

### Step 2: VoiceMeeter Banana Configuration

**Basic Setup:**
1. Set Windows default playback device to "VoiceMeeter Input"
2. Launch VoiceMeeter Banana

**Critical Configuration:**
1. **MENU → System Settings / Options**
2. **Enable "Patch Insert"** (activates "VoiceMeeter Insert Virtual ASIO" 32-channel output)
3. **A1 Output**: Set to your normal DAC/speakers (optional, for monitoring)

**Verification:**
- Play content in Kodi
- VAIO strip should show activity on all 8 level meters
- This confirms 8-channel capture is working

### Step 3: FlexASIO Configuration

**FlexASIO.toml Configuration:**
```toml
backend = "Windows WASAPI"

[input]
channels = 24
sampleRate = 48000

[output]
channels = 24
sampleRate = 48000
bufferSizeSamples = 512
sampleType = "Float32"
```

**Purpose**: Provides ASIO interface for binaural processors to receive the 8-channel stream from VoiceMeeter

### Step 4A: HeSuVi Setup (Free Option)

**Installation:**
1. Install Equalizer APO
2. Download HeSuVi from SourceForge
3. **APO Configurator**: Tick "VoiceMeeter Insert Virtual ASIO → Output A1"
4. **Windows Sound Settings**: Set "VoiceMeeter Insert Virtual ASIO" to 7.1 surround

**Configuration:**
1. Launch HeSuVi
2. **Connection tab**: Select "Virtualization" for Output A1
3. Verify input levels show activity on all 8 channels
4. Choose HRTF profile (Dolby PCEE, etc.)

**⚠️ CRITICAL LIMITATION:**
- **HeSuVi treats channels 7 & 8 as REAR speakers, not HEIGHT**
- Height objects will be audible but localized behind you at shoulder level
- **NO true overhead positioning**

### Step 4B: APL Virtuoso v2 Setup (Professional Option)

**Installation:**
1. Download 14-day trial or purchase ($149 standalone)
2. Requires iLok authorization

**Configuration:**
1. **Input driver**: FlexASIO (12 in, 2 out)
2. **Settings → Input Config**: 7.1.4
3. **Manual channel mapping**:
   - Ch1 = L
   - Ch2 = R  
   - Ch3 = C
   - Ch4 = LFE
   - Ch5 = Ls
   - Ch6 = Rs
   - Ch7 = Top Front L ← **Correctly mapped as HEIGHT**
   - Ch8 = Top Front R ← **Correctly mapped as HEIGHT**
4. **Room preset**: "APL Reference" (or customize)
5. **HRTF**: Choose preferred option (A, B, C, D, or E)

**✅ ADVANTAGE:**
- **Full height channel awareness**
- Objects positioned correctly ABOVE listener
- Professional-grade binaural processing

### Step 5: Head Tracking (Optional Enhancement)

**HeSuVi Options:**
- Windows Sonic head-tracker integration
- Manual yaw/pitch adjustment

**Virtuoso v2 Options:**
- OSC protocol support
- Audeze Maxwell headphones (built-in tracking)
- Bridgehead tracker
- Supperware tracker
- Waves Nx compatibility

### Step 6: Latency Verification

**Expected Latency Chain:**
- Kodi → VoiceMeeter (WASAPI shared): ~10ms
- VoiceMeeter → FlexASIO: ~4ms (512-sample buffer @48kHz)
- Binaural processing: ~2-3ms
- **Total: ~17ms** (well below lip-sync threshold of 40ms)

### Step 7: System Validation

**Test Material**: Dolby "Amaze" Atmos trailer

**HeSuVi Result:**
- Bird circling sounds present
- **No overhead flyover effect** (height mapped to rear)
- Still immersive but lacking vertical dimension

**Virtuoso v2 Result:**
- Bird clearly moves overhead between Top Front speakers
- **Full 3D positioning including height**
- True Atmos experience on headphones

## 🎯 **BINAURAL PROCESSOR COMPARISON**

| Feature | HeSuVi (Free) | APL Virtuoso v2 ($149) |
|---------|---------------|-------------------------|
| **Max Input Channels** | 8 (7.1) | 26 (up to 9.1.6+) |
| **Height Awareness** | ❌ No - treats as rear | ✅ Yes - full 3D positioning |
| **Channel 7/8 Treatment** | Rear Surround | Top Front Height |
| **Overhead Localization** | ❌ Missing | ✅ Accurate |
| **HRTF Quality** | Good | Professional |
| **Room Simulation** | Basic | Advanced (7 presets) |
| **Head Tracking** | Limited | Full support |
| **Cost** | FREE | $149 |
| **5.1.2 Recommendation** | Works but limited | **Recommended** |

## 💡 **KEY FINDINGS & CONCLUSIONS**

### ✅ **What Works Well:**
1. **Kodi delivers clean 5.1.2 PCM** - FFmpeg properly extracts first two height objects
2. **VoiceMeeter routing is reliable** - stable 8-channel bridge to ASIO
3. **Low latency achieved** - ~17ms total, suitable for video content
4. **Free solution exists** - HeSuVi provides basic binaural processing

### ⚠️ **Critical Limitations:**
1. **8-channel maximum** - no access to full 16+ channel Atmos layouts
2. **Height mapping varies by processor**:
   - HeSuVi: Incorrect (rear placement)
   - Virtuoso: Correct (overhead placement)

### 🎯 **Final Recommendation:**

**For Budget-Conscious Users:**
- Start with **HeSuVi (free)** to test the pipeline
- Accept limited height awareness as trade-off
- Still provides significant surround enhancement

**For Quality-Focused Users:**
- Invest in **APL Virtuoso v2** for true height positioning
- 14-day trial available to test before purchase
- Professional-grade binaural processing worth the cost

**For Future-Proofing:**
- Pipeline scales easily to higher channel counts
- When >8 channel solutions emerge, only final processor needs upgrading
- Foundation (Kodi → VoiceMeeter → FlexASIO) remains unchanged

## 🔧 **TROUBLESHOOTING TIPS**

### No Audio in VoiceMeeter:
- Verify Kodi output device matches Windows default
- Check VoiceMeeter VAIO strip for input activity

### Crackling/Dropouts:
- Increase FlexASIO buffer size (1024 samples)
- Close unnecessary background applications
- Check Windows audio exclusive mode settings

### Missing Height Effects:
- Confirm "Allow passthrough" is OFF in Kodi
- Verify 8-channel output in Kodi debug display
- For HeSuVi: accept limitation or upgrade to Virtuoso

### Channel Mapping Issues:
- Double-check VoiceMeeter Insert is enabled
- Verify FlexASIO channel configuration
- Test with known 7.1 content first

---

**Document Status**: Complete implementation guide for 5.1.2 Atmos headphone virtualization  
**Last Updated**: January 2025  
**Next Steps**: Consider testing with alternative media players or investigating >8 channel solutions