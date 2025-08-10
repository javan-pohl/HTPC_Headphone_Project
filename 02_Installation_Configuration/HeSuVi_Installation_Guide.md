# HeSuVi Installation & Configuration Guide (with Impulcifer integration)

Date: January 2025

## Goal
Set up HeSuVi + Equalizer APO to binauralize 7.1 bed PCM from Kodi routed through VoiceMeeter, then integrate personalized in‑ear microphone (HRIR) measurements via Impulcifer for improved spatial accuracy.

---

## Important notes
- HeSuVi runs on Equalizer APO and processes Windows playback devices. It does not take ASIO input directly.
- We will apply HeSuVi on the `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)` playback device so that Kodi’s 7.1 output is virtualized to stereo before routing to the DAC.
- Known limitation: The PCM path from Kodi/LAV is 7.1 bed only (no discrete height channels). HeSuVi virtualizes the bed; overhead cues may appear as rear/shoulder or weak pseudo‑elevation. If overhead accuracy is critical, plan to evaluate Virtuoso v2 after HeSuVi validation.

---

## Prerequisites
- VoiceMeeter Banana installed and working per `02_Installation_Configuration/VoiceMeeter_Installation_Guide.md`.
- Kodi configured to output 7.1 PCM to `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)` per `02_Installation_Configuration/Kodi_HTPC_Optimal_Settings.md`.
- FlexASIO present (not used by HeSuVi directly, but part of the broader test platform).

---

## Step 1 — Configure Windows device for 7.1 on VoiceMeeter Input
1. Right‑click the speaker icon → Sound settings → More sound settings → Playback tab.
2. Select `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)` → Configure → set to 7.1 Surround.
3. Disable all Enhancements on both `VoiceMeeter Input` and your DAC playback devices.
4. Ensure Windows default playback device is `VoiceMeeter Input` (or Kodi selects it explicitly).

Why: Equalizer APO/HeSuVi needs the endpoint in 7.1 so it can receive discrete channels 1–8 before downmixing to binaural stereo.

---

## Step 2 — Install Equalizer APO
1. Download Equalizer APO (latest) and run installer as Administrator.
2. When the Configurator opens:
   - Tick the playback device `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)`.
   - Optionally also tick `VoiceMeeter AUX Input` if you plan to route a second app.
   - Do NOT tick your DAC endpoints if you only want processing on the VAIO input.
3. Reboot when prompted.

Verification: After reboot, run `Configurator.exe` again to confirm the device remains ticked. If audio seems unaffected, re-run the Configurator and ensure `Install as SFX/EFX` is active for the selected device (if shown).

---

## Step 3 — Install HeSuVi
1. Download HeSuVi from SourceForge (latest release).
2. Run installer as Administrator. If prompted, let it “Install/Repair” configuration for Equalizer APO.
3. Launch HeSuVi. The app writes its configuration into Equalizer APO’s `config` folder and manages the active profile.

Folder note (typical): `C:\Program Files\EqualizerAPO\config\HeSuVi` contains HeSuVi presets/HRIRs; `config.txt` includes HeSuVi when enabled.

---

## Step 4 — Basic HeSuVi configuration (7.1 → binaural)
1. Open HeSuVi.
2. Connection / Target device: ensure it is set to the same device where Equalizer APO is active: `VoiceMeeter Input (VB‑Audio VoiceMeeter VAIO)`.
3. Enable Virtualization / 7.1 Surround.
4. HRTF selection: start with a neutral preset (e.g., IRCAM/IRC_1038) or the default.
5. Disable other effects (room, bass boost, crossfeed, etc.) for baseline testing.
6. Save profile.

Expected behavior: Kodi outputs 7.1 bed PCM to the VAIO device. HeSuVi (via E‑APO) virtualizes to stereo, so VoiceMeeter VAIO input meters now show 2 channels. Route to your DAC on A1 as normal.

---

## Step 5 — Verify audio flow and mapping
1. In Kodi, play 7.1 content and press Ctrl+Shift+O → should show `PCM 8‑ch @48 kHz`.
2. In Windows Sound → Playback → `VoiceMeeter Input` → Configure → Test: each channel should image around you on the horizontal plane; overhead cues are not discrete in the PCM path.
3. In HeSuVi, toggle Bypass to A/B the virtualization.
4. In VoiceMeeter, confirm VAIO meters show stereo after virtualization; A1 routes cleanly to DAC.

If you still see 8 channels in VoiceMeeter after enabling HeSuVi, E‑APO is likely not active on the VAIO device—re-run the Configurator and ensure the correct device is ticked.

---

## Step 6 — Latency and lip‑sync
HeSuVi/E‑APO adds modest latency (typically <30 ms). If lip‑sync is off in video playback, apply an audio offset in Kodi (Audio settings → Audio offset; negative values advance audio) until lips match.

---

## Step 7 — Optional: Headphone EQ
If your headphone model exists in HeSuVi’s database, you can enable its EQ. Keep it off initially; add after you lock in virtualization.

---

## Step 8 — Persistence & startup
- Set HeSuVi to auto‑start with Windows and load your saved profile.
- Keep a backup of `C:\Program Files\EqualizerAPO\config\config.txt` after HeSuVi is working.

---

## Step 9 — Integrate in‑ear mic measurements (Impulcifer)

### 9A. Measure and generate filters with Impulcifer
1. Record HRIRs using in‑ear mics per Impulcifer’s guide (speaker positions for your preferred layout; quiet room; correct gain; 48 kHz recommended).
2. In Impulcifer, process the recordings and export an Equalizer APO configuration for 7.1→stereo binaural (this produces a set of WAVs and a `config.txt` for E‑APO’s Convolver).

### 9B. Easiest integration (recommended): use Impulcifer’s E‑APO config directly
Goal: Let Equalizer APO’s Convolver apply your personal HRIRs on the same `VoiceMeeter Input` device. Only one virtualization chain should be active at a time.

Steps:
1. Create a folder, e.g., `C:\Program Files\EqualizerAPO\config\impulcifer\` and place Impulcifer’s exported files there (its `config.txt` and WAVs).
2. Edit `C:\Program Files\EqualizerAPO\config\config.txt`:
   - Comment out the HeSuVi include line.
   - Include the Impulcifer config instead.

Example minimal config.txt (concept):
```
# HeSuVi include (disable when using Impulcifer)
# Include: HeSuVi\HeSuVi.txt

# Impulcifer personal HRTF (enable for measurement-based profile)
Include: impulcifer\config.txt
```

3. Save and restart audio (or reboot) to apply. Verify by A/B listening and using the Windows channel test.

To switch back to HeSuVi, re-enable the HeSuVi include and comment out the Impulcifer include.

### 9C. Optional advanced: Convert to a HeSuVi “User HRIR” set
If you prefer controlling everything from the HeSuVi UI, you can convert/export your HRIRs to a format HeSuVi expects for its HRIR library (specific speaker‑angle WAVs in a designated folder). This requires matching channel positions and file naming conventions per HeSuVi’s documentation. High-level:
1. Generate HRIRs for the 7.1 speaker positions (L, R, C, LFE passthrough/no HRIR, Ls, Rs, Lb, Rb) using your Impulcifer results.
2. Place them under HeSuVi’s `hrir` user folder, following the documented naming.
3. Select the “User” HRIR in HeSuVi. Test with the Windows channel test.

Note: The direct E‑APO Convolver method (9B) is simpler and avoids format mismatches. Use 9C only if you specifically want to remain inside HeSuVi’s preset/room UI.

---

## Troubleshooting
- No change in sound: Re-run Equalizer APO Configurator and ensure `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)` is ticked. Confirm the device is set to 7.1 in Windows.
- Still 8 channels inside VoiceMeeter: HeSuVi not applied on the VAIO device; verify Step 2 and Step 4.
- Distortion/clipping: Reduce preamp in HeSuVi or in E‑APO; keep Kodi volume at 100%.
- Overhead cues weak or behind/shoulder: Expected on the bed‑only PCM path. For stronger elevation, plan to test APL Virtuoso v2 or integrate personal HRIRs via Impulcifer.
- App uses Exclusive mode to DAC bypassing VAIO: Ensure apps output to the VAIO device, not directly to the DAC.

---

## Validation checklist
- [ ] Windows `VoiceMeeter Input` device configured as 7.1
- [ ] Equalizer APO installed and active on `VoiceMeeter Input`
- [ ] HeSuVi Virtualization enabled, target set to `VoiceMeeter Input`
- [ ] Kodi shows `PCM 8-ch @48 kHz` during playback
- [ ] A/B toggle in HeSuVi clearly changes spatialization
- [ ] Optional: Impulcifer config working when enabled; can switch between HeSuVi and Impulcifer by toggling includes

---

## Next step (if HeSuVi proves insufficient)
Test APL Virtuoso v2 (14-day trial) for stronger elevation from bed content and potentially higher spatial fidelity per `00_Project_Status/HTPC_Audio_Setup_Progress_Report.md` and `02_Installation_Configuration/Kodi_5.1.2_Virtualization_Guide.md`. 


