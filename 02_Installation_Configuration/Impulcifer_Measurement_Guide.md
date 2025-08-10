# Impulcifer In‑Ear Measurement Guide (Windows 11 + Master Series Binaural Mics)

Date: January 2025

## Goal
Create personalized HRTFs using in‑ear binaural microphones (Master Series ultra‑low noise, in‑ear microphones) and Impulcifer on Windows 11. Export an Equalizer APO (E‑APO) configuration for 7.1 → stereo binaural virtualization, ready to use per `02_Installation_Configuration/HeSuVi_Installation_Guide.md` Step 9.

---

## What you will achieve
- Record clean binaural impulse responses (HRIRs) for key speaker positions (5.1 or 7.1; plus optional Top Front L/R for 5.1.2)
- Process measurements in Impulcifer
- Export a ready‑to‑use `config.txt` for Equalizer APO’s Convolver
- Validate with Windows channel test and content playback

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
Impulcifer provides a GUI and CLI. Steps are equivalent.

1) Create a project folder
- Example: `C:\\Projects\\impulcifer\\my_hrir_2025_01\\raw\\`

2) Launch Impulcifer and set I/O (Audiophile Settings)
- Input device: your USB interface/recorder (stereo)
- Output device: the playback device feeding your speakers
- **Sample rate**: **192 kHz** (or highest both devices support - match both sides exactly)
- **Bit depth**: **24-bit minimum, 32-bit float preferred**
- Channels: 2 in / 2 out
- **Buffer size**: 1024+ samples for stability
- **Quality check**: Verify no internal resampling in either device

3) Select sweep settings (Maximum Quality)
- **Sweep type**: Log sweep (covers full frequency range efficiently)
- **Duration**: **10–15 seconds** (longer = better SNR, more detail in low frequencies)
- **Frequency range**: **10 Hz to 96 kHz** (for 192kHz capture) - captures beyond audible range for processing headroom
- Fade‑in/out enabled; pre‑silence 0.5 s; post‑silence 0.5–1.0 s
- **Output level**: start at −12 dBFS; confirm no clipping at mics
- **Quality rationale**: Longer sweeps capture more low-frequency detail; extended range preserves all spatial cues

**Bottleneck Alert**: If Impulcifer is limited to 48kHz internal processing, you may need to capture at 192kHz then downsample later with high-quality SRC.

4) Record per position (bed first, then heights)
- Sequence example for 5.1.2: C → L → R → Ls → Rs → (optional Lb → Rb) → TFL → TFR
- For each position:
  - Confirm geometry (angle/elevation/distance)
  - In Impulcifer, select the corresponding label (or note it for file naming)
  - Record 2–3 sweeps; keep the best one (lowest noise, most consistent)

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

5) Export for Equalizer APO (High Quality)
- Export type: Equalizer APO Convolver
- **Sample rate**: Export at **192kHz** (maintain original quality)
- **Bit depth**: **32-bit float** for processing headroom
- Destination folder: `C:\\Program Files\\EqualizerAPO\\config\\impulcifer\\`
- Contents produced:
  - `config.txt` (includes the Convolver routing)
  - **High-resolution IR WAVs** (192kHz/32-bit float)

6) Version your work
- Copy the export to a dated subfolder for rollback
- **Archive raw captures**: Keep original 192kHz recordings for future reprocessing
- Document measurement conditions and settings

**Quality Bottleneck**: EqualizerAPO may downsample internally to 48kHz. For maximum quality Atmos processing, plan to use these HRIRs in a 192kHz-capable convolution engine (custom processing, high-end DAW, or dedicated convolver).

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
- Windows Sound → Playback → `VoiceMeeter Input` (or your target device) → Configure → Test. Each channel should image at the correct virtual location.
- In Impulcifer/E‑APO, bypass vs. engage to A/B. You should hear strong externalization and stable imaging.
- In Kodi, play known 5.1/7.1/Atmos files; press Ctrl+Shift+O to verify `PCM 8‑ch @48 kHz`. Imaging should match expectations.

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
