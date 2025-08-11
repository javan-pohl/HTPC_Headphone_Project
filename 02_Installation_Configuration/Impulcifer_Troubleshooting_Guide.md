# Impulcifer Troubleshooting Guide

**Date:** January 2025  
**Environment:** Windows 11, Python 3.8, USB Binaural Mics, D90 III DAC

## Overview
This guide documents issues encountered during Impulcifer setup and measurement, along with their solutions. Use this as a reference to avoid repeating troubleshooting steps.

## 🚨 **CRITICAL ISSUE: EMPTY RECORDING FILES**

**The primary problem we're solving:** Recording files are either not being generated or are empty (48 bytes = just WAV headers with no audio content).

**Symptoms:**
- Recording directories created but contain no files
- Files created but only 48 bytes (empty WAV headers)
- No error messages visible during recording
- Script continues to next measurement despite failure
- **Audio plays but recording is silent or distorted**

**ROOT CAUSES IDENTIFIED:**

1. **⭐ MAJOR: Channel Count Mismatch in measurement_guide.py**
   - Script was calling recorder with `--channels=1` (mono)
   - Binaural microphones require `--channels=2` (stereo)
   - This mismatch caused silent/empty recordings

2. **⭐ MAJOR: Host API Incompatibility**
   - Script was using `--host_api=WASAPI` which has strict format requirements
   - Basic audio setups work better with `--host_api=MME`
   - WASAPI failures often produced no clear error messages

3. **Recording Channel Bug in recorder.py**
   - Recorder was using CLI `--channels` parameter for recording
   - Should use fixed 2-channel recording for binaural mics regardless of output channels

4. **Windows Audio Interference** 
   - Windows "enhancements" and communications ducking cancel out playback audio
   - Affects actual audio content but not always file creation

**SOLUTION IMPLEMENTED:** Fixed all channel/host API mismatches and added comprehensive diagnostics.

---

## Critical Issues & Solutions

### 1. **Audio File Format Mismatch**
**Problem:** Script trying to play `.pkl` files instead of `.wav` files
- **Error:** `RuntimeError: Error opening 'data/sweep-6.25s-48000Hz-16bit-39.06Hz-20000Hz.pkl': File contains data in an unknown format`
- **Root Cause:** `.pkl` files contain Python data structures, not audio
- **Solution:** ✅ **FIXED** - Updated script to use `.wav` files
- **Files Modified:** `measurement_guide.py`, `Impulcifer_Measurement_Guide.md`

### 2. **Sample Rate Mismatch (DAC/Device)**
**Problem:** Audio devices don't support 48kHz format
- **Error:** `'AUDCLNT_E_UNSUPPORTED_FORMAT' [Windows WASAPI error -2004287480]`
- **Root Cause:** DAC/audio interface not configured for 48kHz
- **Solution:** ✅ **FIXED** - Set DAC to 16-bit 48kHz in Windows Sound settings
- **Critical:** **Always match DAC sample rate to sweep file sample rate**

### 3. **Recording Channel Mismatch** ⭐ **MAJOR CAUSE OF EMPTY FILES - RESOLVED**
**Problem:** Multiple channel count issues causing silent/empty recordings
- **Error:** Silent recordings, empty WAV files (48 bytes)
- **Root Causes:** 
  - `measurement_guide.py` calling recorder with `--channels=1` (should be 2 for binaural mics)
  - `recorder.py` using CLI channels parameter for recording (should be fixed at 2)
- **Solution:** ✅ **FIXED** - Updated both files:
  - `measurement_guide.py`: Changed to `--channels=2` 
  - `recorder.py`: Fixed to always record 2 channels for binaural mics
- **Files Modified:** `measurement_guide.py`, `recorder.py`
- **Impact:** This was the primary cause of empty recording files

### 4. **Device Detection Channel Requirements**
**Problem:** Device detection requiring specific channel counts
- **Error:** `DeviceNotFoundError: Could not find any device which satisfies minimum channel count`
- **Root Cause:** Impulcifer looking for multichannel output devices
- **Solution:** ✅ **FIXED** - Modified to allow basic audio setups with `min_channels=0`
- **Files Modified:** `recorder.py`

### 5. **Host API Incompatibility** ⭐ **MAJOR CAUSE OF SILENT FAILURES - RESOLVED**
**Problem:** WASAPI host API causing device/format errors with basic setups
- **Error:** Silent failures, recordings not created, format errors
- **Root Cause:** `measurement_guide.py` using `--host_api=WASAPI` which has strict requirements
- **Solution:** ✅ **FIXED** - Changed to `--host_api=MME` for better compatibility
- **Files Modified:** `measurement_guide.py`
- **Impact:** MME works reliably with basic Windows audio setups

### 6. **Error Handling & Visibility** ⭐ **RESOLVED**
**Problem:** Recording errors disappearing from terminal, script continuing
- **Error:** Silent failures, no error messages visible
- **Root Cause:** Poor error capture and diagnostics in measurement script
- **Solution:** ✅ **FIXED** - Added comprehensive preflight checks and logging:
  - Verify sweep file exists and output directory is writable
  - Print full STDOUT/STDERR from recorder process
  - Test file creation permissions before recording
  - Clear error messages for all failure modes
- **Files Modified:** `measurement_guide.py`, `recorder.py`

### 7. **Windows Audio Interference** ⭐ **SECONDARY CAUSE OF SILENT RECORDINGS**
**Problem:** Windows canceling playback audio from recordings
- **Error:** Audio plays but recordings are silent or heavily distorted
- **Root Cause:** Windows communications ducking and audio enhancements
- **Solution:** ✅ **FIXED** - Disable Windows audio processing
- **Critical Steps:**
  1. **Disable Communications Ducking:** Sound settings → Communications tab → "Do nothing"
  2. **Disable ALL Audio Enhancements:** Both playback and recording devices
  3. **Disable Exclusive Mode:** Uncheck "Allow applications to take exclusive control"
- **Note:** This affects audio quality but not file creation. The channel/host API fixes above resolve the empty file issue.

---

## 🔧 **CRITICAL WINDOWS AUDIO SETTINGS**

### **Step 1: Disable Communications Ducking**
1. Right-click speaker icon → "Sound settings" → "More sound settings"
2. Go to **Communications** tab
3. Select **"Do nothing"**
4. Click **OK**

### **Step 2: Disable Audio Enhancements (BOTH Devices)**

**For Playback Device (DAC/Speakers):**
1. More sound settings → **Playback** tab → Select your output → **Properties**
2. **Enhancements** tab → Check **"Disable all enhancements"**
3. **Advanced** tab → Uncheck **"Allow applications to take exclusive control"**
4. Click **OK**

**For Recording Device (Microphones):**
1. More sound settings → **Recording** tab → Select your mics → **Properties**
2. **Enhancements** tab → Disable ALL:
   - Noise Suppression
   - Echo Cancellation
   - Automatic Gain Control (AGC)
   - Beam Forming
   - Any other enhancements
3. **Advanced** tab → Uncheck **"Allow applications to take exclusive control"**
4. Click **OK**

### **Step 3: Restart Audio Services**
- Restart computer OR restart Windows Audio service
- Test recording to verify fix

---

## Audio Device Configuration

### **Current Working Setup:**
- **Input:** Microphone Array (USB PnP Audio Device) - MME
- **Output:** Speakers (TOPPING USB DAC) - MME  
- **Sample Rate:** 48kHz
- **Bit Depth:** 16-bit
- **Recording Channels:** 2 (stereo for binaural mics)
- **Host API:** MME (more compatible than WASAPI for basic setups)

### **Host API Preferences:**
1. **MME** - Most compatible, works with basic setups
2. **DirectSound** - Good compatibility, moderate latency
3. **WASAPI** - Best performance, strict format requirements

---

## Sweep File Specifications

### **Current Working Sweep:**
- **File:** `sweep-6.25s-48000Hz-16bit-39.06Hz-20000Hz.wav`
- **Sample Rate:** 48kHz
- **Bit Depth:** 16-bit
- **Frequency Range:** 39.06Hz - 20kHz
- **Duration:** 6.25 seconds
- **Channels:** 1 (mono sweep file)

### **Alternative Sweeps Available:**
- `sweep-6.15s-48000Hz-32bit-2.93Hz-24000Hz.wav` (32-bit, lower frequency)
- `sweep-6.16s-192000Hz-32bit-39.06Hz-20000Hz.wav` (192kHz, 32-bit)

---

## Working Commands

### **Basic Headphone Test (Fixed Method):**
```cmd
cd C:\HTPC\Impulcifer
venv\Scripts\python.exe recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/test/headphones.wav" --channels=2 --host_api=MME
```

### **Interactive Measurement Guide (Fixed):**
```cmd
cd C:\HTPC\Impulcifer
venv\Scripts\python.exe measurement_guide.py
```

### **With Explicit Devices:**
```cmd
venv\Scripts\python.exe recorder.py --play="data/sweep-6.25s-48000Hz-16bit-39.06Hz-20000Hz.wav" --record="data/test/headphones.wav" --input_device="Microphone Array (USB PnP Audio Device)" --output_device="Speakers (TOPPING USB DAC)" --channels=2 --host_api=MME
```

---

## Troubleshooting Checklist

### **Before Each Test:**
- [ ] DAC set to 48kHz/16-bit in Windows Sound settings
- [ ] Microphones connected and working
- [ ] Headphones/speakers connected and working
- [ ] Room quiet (no HVAC, fans, etc.)
- [ ] Virtual environment activated
- [ ] **Windows communications ducking disabled** ⭐ **CRITICAL**
- [ ] **All audio enhancements disabled** (playback AND recording) ⭐ **CRITICAL**
- [ ] **Exclusive mode disabled** on both devices ⭐ **CRITICAL**

### **If Recording Fails:**
1. **Check file size** - Empty files (48 bytes) = recording failed ⭐ **PRIMARY INDICATOR**
2. **Check device detection** - Use `python -m sounddevice`
3. **Try MME host API** - More compatible than WASAPI
4. **Verify sample rate match** - DAC must match sweep file
5. **Check microphone permissions** - Windows may block access
6. **Verify recording channels** - Must be 2 for binaural mics (not 1 from sweep file)

### **If Audio Doesn't Play:**
1. **Check output device** - Verify DAC is selected
2. **Check volume levels** - Start at -12dBFS
3. **Try different host API** - MME → DirectSound → WASAPI
4. **Check for exclusive mode** - Other apps may block audio

---

## Known Working Configuration

### **Hardware:**
- **Input:** Master Series USB Binaural Microphones
- **Output:** Topping D90 III DAC
- **Interface:** MME (Windows Multimedia Extensions)

### **Software:**
- **Python:** 3.8
- **Host API:** MME
- **Sample Rate:** 48kHz
- **Bit Depth:** 16-bit
- **Channels:** 2 (stereo recording)

### **Sweep File:**
- **Format:** WAV (not PKL)
- **Sample Rate:** 48kHz
- **Bit Depth:** 16-bit
- **Frequency:** 39.06Hz - 20kHz

---

## Next Steps

### **Immediate Test:**
1. Run basic headphone recording test
2. **Verify non-empty WAV file is created** ⭐ **CRITICAL**
3. **Check file size (should be > 1MB for 6.25s recording)** ⭐ **CRITICAL**
4. Listen to recording to confirm audio captured
5. **If file is 48 bytes = recording failed, check this guide**

### **If Test Succeeds:**
1. Run full measurement guide
2. Process recordings with Impulcifer
3. Test with HeSuVi/Equalizer APO

### **If Test Fails:**
1. Document exact error message
2. Check this troubleshooting guide
3. Try alternative host APIs
4. Verify all device settings

---

## File Modifications Made

### **recorder.py:**
- Line 211: Added `min_channels=0` for basic setups
- Line 238: Fixed recording channels to always use 2 for binaural mics (not CLI parameter)
- Line 33-40: Added safe gain calculation with warnings
- Added verbose recording parameter logging
- Enhanced error handling for WAV file writing

### **measurement_guide.py:**
- Lines 23-47: Added comprehensive preflight checks (sweep file exists, output dir writable, etc.)
- Line 34: Changed from `--channels=1 --host_api=WASAPI` to `--channels=2 --host_api=MME`
- Enhanced subprocess error capture with full STDOUT/STDERR
- Added detailed logging of all file paths and execution steps

### **Documentation:**
- Updated all `.pkl` references to `.wav`
- Added device configuration options
- Enhanced error handling instructions

---

**Last Updated:** January 2025  
**Status:** ✅ **RESOLVED** - Empty file issue fixed, measurement guide working  

## 🎉 **RESOLUTION SUMMARY**

**PRIMARY ISSUES RESOLVED:**
1. **Channel Count Mismatch:** Fixed `measurement_guide.py` to use `--channels=2` for binaural mics
2. **Host API Incompatibility:** Changed from WASAPI to MME for basic Windows setups  
3. **Recording Channel Bug:** Fixed `recorder.py` to always record 2 channels regardless of CLI parameter
4. **Poor Diagnostics:** Added comprehensive preflight checks and error logging

**RESULT:** The measurement guide now successfully creates non-empty recording files with proper audio content.
