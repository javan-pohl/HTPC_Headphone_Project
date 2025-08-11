# Impulcifer In‑Ear Measurement Guide (Windows 11 + Master Series USB Binaural Mics)

Date: January 2025  
**Updated with optimized settings and speaker-safe parameters**

## Goal
Create personalized HRTFs using in‑ear binaural microphones (Master Series USB binaural mics) and Impulcifer on Windows 11. Export an Equalizer APO (E‑APO) configuration for 7.1 → stereo binaural virtualization, ready to use per `02_Installation_Configuration/HeSuVi_Installation_Guide.md` Step 9.

## Quick Setup Summary (Our Configuration)
- **Target Layout**: 9.1.6 (9 bed channels + 6 height channels)
- **Microphones**: Master Series USB binaural mics (no external power needed)
- **Sample Rate**: 48kHz (matches USB microphone capability)
- **Frequency Range**: 78Hz - 20kHz (speaker-safe + optimized bass response)
- **Sweep Files**: 
  - `sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav` (mono, for single speaker measurements)
  - `sweep-seg-FL-mono-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav` (headphone measurements)
  - `sweep-seg-FL,FR-stereo-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav` (stereo headphone measurements)
- **Installation**: `C:\HTPC\Impulcifer\` with Python 3.8 virtual environment
- **Processing**: Command-line operation for precise control
- **Total Measurements**: 16 positions (15 HRIRs + 1 headphone compensation)

---

## What you will achieve
- Record clean binaural impulse responses (HRIRs) for **9.1.6 layout** (15 speaker positions)
- **Full immersive coverage**: 9 bed channels + 6 overhead channels for complete 3D audio
- Process measurements in Impulcifer at audiophile 192kHz quality
- Export a ready‑to‑use HRTF set for advanced surround processing
- Validate with Windows channel test and 9.1.6 Atmos content playback

---

## Prerequisites

### Hardware
- Master Series in‑ear binaural microphones (matched stereo pair)
- Microphone power/interface, one of:
  - USB audio interface with microphone inputs and phantom power + the mic maker’s phantom‑to‑plug‑in‑power adapter (“battery box”/power module), or
  - Portable recorder that provides plug‑in power (e.g., Zoom/Tascam) + USB audio interface mode to laptop, or
  - Dedicated plug‑in‑power USB mic interface (stereo) for electret capsules
- Windows 11 laptop (quiet power profile; ideally on battery to reduce ground loops)
- Playback speakers you can place at defined angles (nearfield monitors ideal); quiet room
- Stands/tape/laser measure for consistent distance/height; chair you can rotate smoothly
- Headphones for later validation

### Software
- Impulcifer (latest)
  - Option A: GUI release for Windows (preferred if available)
  - Option B: Python tools (Python 3.10+), `pip install impulcifer`
- Equalizer APO (installed) and HeSuVi (optional), see `HeSuVi_Installation_Guide.md`
- Optional utilities: REW (level checks), LatencyMon (system stability), Voicemeeter (routing)

---

## Preparation & safety
- Keep sweep playback moderate. Target peak levels around −12 dBFS at your recorder. Avoid discomfort.
- Insert mics securely and symmetrically; cable strain relief to avoid handling noise.
- Quiet room: turn off HVAC, fridges, fans, phones. Perform measurements late at night if possible.
- Power hygiene: prefer laptop battery; if you must charge, use a grounded charger or an isolation transformer on the speaker amp as appropriate. Avoid USB hubs during capture.

---

## Windows and device configuration (Audiophile Quality)
1. **Set maximum sample rate supported by your hardware**:
   - Check your interface capabilities: 48, 96, 192 kHz (use highest available)
   - Sound settings → your recording device → Advanced → **192000 Hz, 24‑bit** (or highest supported)
   - Playback device feeding the speakers → **same rate as recording device**
   - **Quality rationale**: Higher sample rates capture more spatial detail above 20kHz, preserve transient accuracy
2. Disable all Enhancements/Sound Effects on both record and playback devices.
3. Exclusive mode: enable "Allow applications to take exclusive control" for both playback/record devices (Impulcifer may request it).
4. In your USB interface/recorder control panel:
   - **Sample rate**: Set to maximum (192kHz preferred, 96kHz minimum)
   - **Bit depth**: 24-bit minimum, 32-bit float if available
   - **Buffer size**: Larger buffers (1024+ samples) for stability during measurement
   - Phantom power ON only if your power module needs it (never feed 48 V directly to bare 3.5 mm electret mics).
   - Gain: start low; we will calibrate.

**Quality Bottleneck Alert**: Some USB interfaces downsample internally or use poor ADC/DAC at high sample rates. Verify your interface maintains quality at 192kHz (check specs/reviews).

---

## Physical geometry (layouts)
Choose a target layout to capture. Minimum viable for height is 5.1.2. If you only capture 7.1 bed (no heights), you can still virtualize standard surround.

- Speaker height: ear height for bed channels; 30–45° elevation for Top Front heights.
- Listener: seat at reference point; head upright; eyes forward at 0° azimuth.
- Distance: 1.0–1.5 m typical in a small room; keep it consistent across positions.

Recommended angles (azimuth°, elevation°):
- L/R: ±30°, 0°
- C: 0°, 0°
- LFE: no HRIR (pass‑through)
- Ls/Rs: ±90°, 0°
- Lb/Rb (7.1 optional): ±150°, 0°
- Top Front L/R (5.1.2): ±30°, +30–40° elevation

Tip: If you have only two speakers, you can move them (or rotate yourself) to each angle in turn. Consistency matters more than perfection.

### Height channels: importance and options
- Elevation cues benefit from personalized height captures but are not mandatory for a strong result. Bed-only (5.1/7.1) gives excellent horizontal imaging; elevation will be weaker.
- Minimal height set: capturing only Top Front Left/Right (TFL/TFR) is enough for convincing 5.1.2 elevation.
- No mounts? Recline to simulate height: if you recline your torso/head by ~35–40°, speakers at ear height become “top-front” relative to your ears. Keep the head rigid, insertion depth identical, and use longer sweeps (7–10 s). In processing, prefer short time-windowing to focus on the direct sound.
- Skip heights now, add later: measure the full bed today; you can add just TFL/TFR on a later date and re-export within minutes.
- Borrow a theater if desired: a quick session elsewhere to capture two height positions (TFL/TFR) is sufficient; keep levels and geometry consistent.
- Minimize room influence: quiet room, stable head, laptop on battery if possible, consistent speaker distance; time-window early IRs during processing to reduce reflections.

---

## Recording strategy (pick one)
You need separate sweeps for each virtual speaker position, recorded binaurally (both ears simultaneously). Choose the method that fits your room and gear.

1) Fixed speakers, rotate the listener (fastest with two speakers)
- Place two speakers symmetrically at ±30° (ear height). Mark chair center on floor.
- For each target azimuth, rotate the chair to align the head toward the intended angle while keeping speakers fixed. For surrounds/rears, rotate accordingly to simulate ±90°, ±150°.
- For heights: elevate the speakers to +35° and repeat rotations for Top Front L/R positions.

2) Move a single speaker to each angle
- Keep your head strictly forward at 0°.
- Place the speaker at each target azimuth/elevation using a protractor/laser. Repeat for left/right as needed.

3) Move two speakers between angle pairs (reduces moves)
- Similar to (2) but reposition a stereo pair for each angle set.

Notes
- Keep the mic insertion depth and orientation identical across all captures.
- Use a chin rest or head brace if possible to avoid micro‑movements during sweeps.

---

## Level calibration
- Start with speakers at a comfortable volume.
- Arm the recording device in Impulcifer (or your DAW/interface mixer) and play pink noise or a short sweep at −20 dBFS.
- Adjust preamp gain so peaks land around −12 dBFS; absolute peaks below −6 dBFS. No red clipping at any time.
- Maintain the same gain for the entire session.

---

## Capture with Impulcifer
Impulcifer provides a GUI and CLI. We'll use CLI for precise control.

1) Create a project folder
- Example: `C:\\HTPC\\Impulcifer\\data\\my_hrir_2025_01\\`

2) Hardware Setup (Simplified USB Setup)
- **Microphones**: Master Series USB binaural microphones (no external power needed)
- **Input device**: Your USB microphones (stereo)
- **Output device**: Windows playback device feeding your speakers
- **Verify USB mics** appear in Windows Sound → Recording as stereo device

3) Hardware-Matched Sweep Settings (Optimized for Your Setup)
- **Pre-generated sweeps**: Available in `data/` directory
  - `sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav` (mono, for single speaker measurements)
  - `sweep-seg-FL-mono-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav` (for headphone measurements)
  - `sweep-seg-FL,FR-stereo-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav` (stereo headphone option)
- **Sample rate**: **48 kHz** (matches USB microphone capability)
- **Bit depth**: **16-bit** (matches USB microphone capability)
- **Frequency range**: **78.12 Hz to 20 kHz** (speaker-safe + optimized bass response)
- **Duration**: **6.03 seconds** (optimal SNR vs practicality)
- **Output level**: start at −12 dBFS; confirm no clipping at mics
- **Quality**: Hardware-matched for cleanest signal chain and maximum measurement accuracy

### Creating Custom Sweep Files (Advanced)

If you need different sweep parameters, you can generate custom sweep files using Impulcifer's built-in sweep generator:

**Before generating new sweeps**, you need to modify the frequency limits in `impulse_response_estimator.py`:

1. **Edit frequency range** (lines 25-31 in `impulse_response_estimator.py`):
   ```python
   # End frequency is 20kHz maximum (human hearing limit and speaker protection)
   self.high = min(20000, self.fs / 2)
   
   # Start frequency calculation - modify target_low for different bass response:
   target_low = 78  # Change this value for different starting frequency
   self.n_octaves = np.floor(np.log2(self.high / target_low))
   self.low = self.high / 2**self.n_octaves
   ```
   
   **Common target_low values:**
   - `target_low = 78` → actual: ~78Hz (current setting, speaker-safe)
   - `target_low = 50` → actual: ~46Hz (more bass extension)
   - `target_low = 100` → actual: ~156Hz (very speaker-safe)

2. **Generate sweep files** using the command line:

   **For mono speaker measurements:**
   ```cmd
   venv\Scripts\python.exe impulse_response_estimator.py --dir_path=data --fs=48000 --duration=6.0 --bit_depth=16 --speakers=FL --tracks=mono
   ```

   **For stereo headphone measurements:**
   ```cmd
   venv\Scripts\python.exe impulse_response_estimator.py --dir_path=data --fs=48000 --duration=6.0 --bit_depth=16 --speakers=FL,FR --tracks=stereo
   ```

   **Command parameters:**
   - `--dir_path=data`: Output directory for sweep files
   - `--fs=48000`: Sample rate (match your microphones)
   - `--duration=6.0`: Sweep length in seconds
   - `--bit_depth=16`: Bit depth (match your microphones)
   - `--speakers=FL` or `FL,FR`: Channel configuration
   - `--tracks=mono` or `stereo`: Output format

3. **Generated files** will be named automatically:
   - Mono: `sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav`
   - Stereo: `sweep-seg-FL,FR-stereo-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav`
   - Mono segment: `sweep-seg-FL-mono-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav`

4. **Update measurement commands** to use your new sweep file name in all recording commands below.

**Why customize sweep parameters?**
- **Lower frequency**: Better bass response but may stress small speakers
- **Higher frequency**: Safer for small speakers but less bass information
- **Longer duration**: Better signal-to-noise ratio but higher risk of head movement
- **Higher sample rate**: More frequency detail but larger files and processing time

4) Command-Line Operation
Navigate to Impulcifer directory and activate virtual environment:
```cmd
cd C:\HTPC\Impulcifer
.\venv\Scripts\activate.bat
```

5) Recording Commands (Use Our Optimized Sweep)

**First: Record headphone compensation (mics in ears, headphones on)**
```cmd
python recorder.py --play="data/sweep-seg-FL-mono-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/headphones.wav"
```

**Then: Record each speaker position (sequence for 9.1.6)**
**Recording order: Bed channels first, then heights**
- FC → FL → FR → WL → WR → SL → SR → BL → BR → TFL → TFR → TML → TMR → TBL → TBR

For each position:
- Position speaker at correct angle/elevation/distance  
- Insert mics in ears, head upright, eyes forward
- Run recording command:

### BED CHANNELS (9.1):

**Front Center (0°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/FC.wav"
```

**Front Left (-30°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/FL.wav"
```

**Front Right (+30°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/FR.wav"
```

**Wide Left (-60°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/WL.wav"
```

**Wide Right (+60°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/WR.wav"
```

**Side Left (-90°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/SL.wav"
```

**Side Right (+90°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/SR.wav"
```

**Back Left (-150°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/BL.wav"
```

**Back Right (+150°, 0°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/BR.wav"
```

### HEIGHT CHANNELS (.6):

**Top Front Left (-30°, +35°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/TFL.wav"
```

**Top Front Right (+30°, +35°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/TFR.wav"
```

**Top Middle Left (-90°, +90°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/TML.wav"
```

**Top Middle Right (+90°, +90°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/TMR.wav"
```

**Top Back Left (-150°, +35°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/TBL.wav"
```

**Top Back Right (+150°, +35°):**
```cmd
python recorder.py --play="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --record="data/my_hrir_2025_01/TBR.wav"
```

**Note**: LFE channel requires no HRIR measurement (passthrough)

5) File naming
- Use clear names. Example:
  - `C_0_0.wav`
  - `L_-30_0.wav` / `R_30_0.wav`
  - `Ls_-90_0.wav` / `Rs_90_0.wav`
  - `Lb_-150_0.wav` / `Rb_150_0.wav` (optional)
  - `TFL_30_35.wav` / `TFR_-30_35.wav`

6) Sanity check
- Play back a recorded sweep file: you should clearly hear sweep content with obvious L/R ear differences.
- If hum/noise present, see Troubleshooting.

---

## Process in Impulcifer (Audiophile Quality)
1) Load the recorded WAVs
- Map each file to its speaker position in the project.
- **Verify**: Confirm sample rate and channel order (L=left ear, R=right ear).
- **Quality check**: Ensure no automatic sample rate conversion occurred during import.

2) Deconvolution / IR extraction (High Quality Settings)
- **Window settings**: Use appropriate windowing to minimize artifacts (Hann or Blackman-Harris)
- **IR length**: Use full-length IRs (don't truncate) - typically 1000+ taps at 192kHz
- **Noise floor**: Set deconvolution noise floor appropriately (-60dB typical)
- Run the deconvolution to generate HRIRs from your sweeps.
- **Quality inspection**: 
  - Check impulse alignment (left vs. right) and tail noise
  - Verify frequency response extends to expected range
  - Re‑capture any outliers or poor SNR measurements

3) Equalization target (Preserve Detail)
- **Minimal processing**: Start with "no EQ" to preserve maximum detail
- If EQ needed: diffuse‑field or gentle tilt above 2kHz
- **Avoid**: Aggressive EQ that may mask spatial cues

4) Channel set assembly (Extended Layouts)
- **Target for Atmos processing**: Build 7.1.4 set if you measured heights:
  - Bed: L, R, C, LFE passthrough, Ls, Rs, Lb, Rb
  - Heights: TFL, TFR, TBL, TBR (Top Front L/R, Top Back L/R)
- **Fallback**: 7.1 or 5.1.2 if limited measurements
- Ensure LFE is set to passthrough/no HRIR in the export
- **Quality preservation**: Export at original measurement sample rate (192kHz)

6) Processing Command (Generate HRTFs)

**Process all recordings into HRTFs:**
```cmd
python impulcifer.py --test_signal="data/sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav" --dir_path="data/my_hrir_2025_01" --fs=48000 --plot
```

**Key parameters:**
- `--test_signal`: Our hardware-matched sweep file
- `--dir_path`: Folder containing your recordings
- `--fs=48000`: Maintain 48kHz throughout processing (matches microphone)
- `--plot`: Generate analysis graphs

7) Export for Equalizer APO (Hardware-Matched Quality)
- **Automatic export**: Impulcifer creates Equalizer APO files automatically
- **Sample rate**: **48kHz** (matches microphone capability)
- **Bit depth**: **32-bit float** for processing headroom
- **Output files**:
  - `hrir.wav`: Hardware-matched impulse responses
  - `hesuvi.wav`: Compatible with HeSuVi
  - Analysis plots (if `--plot` used)

8) Version your work
- Copy the export to a dated subfolder for rollback
- **Archive raw captures**: Keep original 48kHz recordings for future reprocessing
- Document measurement conditions and settings

**Processing Note**: Since our HRTFs are already at 48kHz, they'll integrate seamlessly with EqualizerAPO and Cavern processing. The hardware-matched approach ensures optimal signal chain performance.

---

## Enable in Equalizer APO
Follow the simple include toggle described in `HeSuVi_Installation_Guide.md` Step 9:

Example `C:\\Program Files\\EqualizerAPO\\config\\config.txt` snippet:
```
# Include one virtualization chain at a time
# Include: HeSuVi\\HeSuVi.txt
Include: impulcifer\\config.txt
```
Restart audio (or reboot) after saving.

---

## Validation

**Test your custom HRTFs:**

1) **Copy files to Equalizer APO:**
```cmd
copy "data\my_hrir_2025_01\hesuvi.wav" "C:\Program Files\EqualizerAPO\config\HeSuVi\hrir\my_custom_hrir.wav"
```

2) **Windows Audio Test:**
- Windows Sound → Playback → Your device → Configure → Test
- Each channel should image at the correct virtual location
- Should feel externalized, not "inside your head"

3) **Compare with HeSuVi:**
- In HeSuVi: select "my_custom_hrir.wav" from Common HRIRs list
- A/B test: bypass vs. engage
- You should hear strong externalization and precise imaging

4) **Content Validation:**
- Play known 5.1/7.1/Atmos content in Kodi
- Verify processing: Ctrl+Shift+O should show PCM multichannel
- Imaging should match your measured speaker positions exactly

**Success indicators:**
- ✅ Sound appears to come from outside your head
- ✅ Center channel stays center when you turn your head
- ✅ Surround channels clearly behind you  
- ✅ Height channels elevated above ear level

---

## Troubleshooting
- No signal or very low level
  - Check plug‑in power/phantom‑to‑PiP adapter is in the chain; verify interface gain.
  - Confirm correct input device and channel mapping (L ear on left channel).
- Hum/buzz (50/60 Hz)
  - Run laptop on battery during capture; avoid ground loops; remove USB hubs; try different outlet for amp.
- Clipping or harsh sound
  - Lower sweep output by 6 dB; lower preamp gain; keep peaks below −6 dBFS.
- Asymmetry (images skew to one side)
  - Re‑seat mics to identical depth; re‑measure Left/Right pairs; verify equal distances to speakers.
- Poor height localization
  - Ensure elevation ~35° and sufficient vertical separation from ear height; reduce ceiling reflections (absorption panel temporarily helps).
- Inconsistent results between takes
  - Stabilize your head; reduce room noise; increase sweep length to 10 s; average multiple IRs if supported.

---

## Best practices & tips
- Consistency beats perfection: keep geometry, level, and mic insertion identical.
- Longer sweeps improve SNR but magnify head‑movement risk; 7–10 s is a good compromise.
- Capture multiple takes per position; archive all raw sweeps for future reprocessing.
- Consider adding Top Rear L/R later for 5.1.4 virtualization if your processor supports it.

---

## Appendix A — Quick checklists

Session checklist
- Mics inserted, cables strain‑relieved
- Interface gain set, 48 kHz confirmed, enhancements off
- Room quiet, laptop on battery
- Speaker angles/height/distance marked
- Test sweep at −12 dBFS peak, no clipping

Capture order (5.1.2)
- C → L → R → Ls → Rs → TFL → TFR (→ Lb → Rb optional)

Files to keep
- `raw/` all takes
- `project/` Impulcifer project file
- `export/` dated E‑APO exports

---

## Appendix B — Integrating with this project
- After export, enable the Impulcifer include per this guide and `HeSuVi_Installation_Guide.md`.
- Use the Validation checklist at the end of `HeSuVi_Installation_Guide.md` to confirm.
- Keep both HeSuVi and Impulcifer chains available; toggle by commenting one include at a time.

---

## FAQ
- Do I need a calibrated SPL meter?
  - Helpful but not required. Relative level consistency matters most.
- Can I measure with only one physical speaker?
  - Yes. It's slower but perfectly valid if you maintain geometry and mic placement.
- What about LFE?
  - Export as passthrough/no HRIR. Binaural processing rarely benefits from LFE HRIRs.
- **192kHz vs 48kHz measurement - does it matter?**
  - **Yes for audiophile applications**: 192kHz captures spatial detail above 20kHz that contributes to localization precision and "air"
  - Preserves transient accuracy critical for realistic soundstage
  - Future-proofs for high-resolution processing chains
  - Only downsample if final processing chain is bottlenecked
- **Will my USB interface actually deliver 192kHz quality?**
  - Check specifications: many "192kHz capable" interfaces use poor ADC/DAC at high rates
  - Verify: low THD+N, flat frequency response to 40kHz+, minimal jitter
  - Test: record and analyze a known high-frequency signal
- **Processing bottlenecks to watch for:**
  - **Impulcifer**: May internally process at lower rates
  - **EqualizerAPO**: Limited to 48kHz processing
  - **Windows Audio**: May resample unless using exclusive mode
  - **Solution**: Keep raw 192kHz captures for direct convolution in high-quality processors

---

## Next steps
- Use this Impulcifer export now, then compare later with APL Virtuoso v2 for height mapping quality (see `00_Project_Status/HTPC_Audio_Setup_Progress_Report.md`).
- When satisfied, back up `C:\\Program Files\\EqualizerAPO\\config\\config.txt` and the entire `impulcifer\\` folder.
