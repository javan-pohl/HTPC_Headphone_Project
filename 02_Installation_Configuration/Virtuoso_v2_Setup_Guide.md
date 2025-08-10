# APL Virtuoso v2 Setup & Height Handling Guide (Windows 11)

Date: January 2025

## Goal
Configure APL Virtuoso v2 as the binaural processor for your HTPC pipeline, clarify how it handles height information, and integrate (where possible) personalized HRTF measurements. Provide clear expectations and alternatives if true height/object rendering is not available in this path.

---

## What Virtuoso v2 can and cannot do in this pipeline
- Input type: Multichannel PCM via Windows audio (through routing software). In your setup, this is 7.1 bed PCM from Kodi/LAV.
- Binauralization: Converts multichannel PCM to stereo for headphones using its virtualization engine and HRTF presets.
- Height channels: Requires discrete height channels in the input to render true top/front/rear speakers. With 7.1 bed PCM, there are no discrete height channels present.
- Object metadata: Does not decode Dolby Atmos objects. Atmos objects are only rendered by licensed Dolby renderers (e.g., Dolby Access, AVR). Virtuoso operates on the channel-based input it receives.

Bottom line in this setup: Virtuoso improves spatialization of the 7.1 bed and may yield stronger elevation impressions than HeSuVi from bed content, but it does not render true Atmos objects or discrete height channels unless you feed it a stream that actually contains them.

---

## Prerequisites
- Windows 11 laptop, 48 kHz system pipeline recommended
- Kodi configured for 7.1 bed PCM to `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)` (see `Kodi_HTPC_Optimal_Settings.md`)
- VoiceMeeter Banana installed, routing Kodi → VoiceMeeter (see `VoiceMeeter_Installation_Guide.md`)
- ASIO driver available for routing to Virtuoso (ASIO4ALL or FlexASIO)
- Headphones and DAC connected (A1 in VoiceMeeter typically routes to the DAC)

Optional
- Personalized HRIRs from Impulcifer (see `Impulcifer_Measurement_Guide.md`)

---

## Recommended routing (7.1 bed PCM → Virtuoso → DAC)
There are multiple valid routings depending on available device drivers and Virtuoso I/O options. Use one of the following.

### Option A — VoiceMeeter Virtual ASIO as Virtuoso input (preferred if available)
- Kodi → `VoiceMeeter Input (VAIO)` → VoiceMeeter strips show 8-ch activity
- In Virtuoso: set input device to `VoiceMeeter Virtual ASIO` (8 inputs) and select 48 kHz
- In Virtuoso: set output device to your DAC (2-ch) or a WDM/WASAPI endpoint that ultimately reaches the DAC
- In VoiceMeeter: mute direct A1 path from VAIO strip to avoid double-feed; listen to Virtuoso’s 2-ch output

### Option B — ASIO4ALL/FlexASIO bridge
- Kodi → `VoiceMeeter Input (VAIO)`
- In Virtuoso: set input device to `ASIO4ALL` (or `FlexASIO`) and enable the 8 inputs that correspond to the VoiceMeeter signal path (this may require ASIO/WDM bridging depending on your exact driver stack)
- Output: select your DAC as Virtuoso’s output device (2-ch)

Notes
- Keep the entire chain at 48 kHz to prevent resampling and lip-sync drift.
- Ensure only one path reaches the DAC (either Virtuoso’s output or VoiceMeeter’s direct A1), not both.

---

## Virtuoso configuration for binaural playback
1) Sample rate and buffer
- 48 kHz, buffer size 256–512 samples to balance stability and latency

2) Channel layout
- Select 7.1 input layout in Virtuoso
- Verify channel mapping: L, R, C, LFE, Ls, Rs, Lb, Rb

3) HRTF/virtualizer profile
- Start with built-in HRTF presets (e.g., A/B/C) and pick the one that yields best externalization
- Headphone EQ: enable or load profile for your headphone model if provided

4) Level and headroom
- Keep Kodi volume at 100%
- In Virtuoso, set input trim/preamp to avoid clipping (target −6 dBFS peaks)

5) Lip-sync
- Measure end-to-end latency and apply a negative Audio offset in Kodi to align lips (see `HeSuVi_Installation_Guide.md` Step 6 for offset guidance)

---

## Height handling: what to expect
- With 7.1 bed PCM input, Virtuoso does not receive discrete height channels. Any perceived elevation comes from its HRTF-based virtualization of bed channels, not from true Top/Height speakers.
- If you later feed Virtuoso a stream containing discrete heights (e.g., 5.1.2/7.1.4 PCM from a DAW/test generator), map those channels in Virtuoso and it will render elevation accordingly. Typical consumer playback paths on Windows do not provide such PCM today from media players.
- For true Atmos object rendering, use Dolby Access or an AVR; Virtuoso does not process object metadata.

---

## Using personalized measurements (Impulcifer) with Virtuoso
Support for direct import of external HRIR/BRIR depends on Virtuoso’s current feature set. Two approaches:

- If Virtuoso supports user IRs/BRIR import:
  - Export your Impulcifer results as stereo BRIRs per position or a composite filter set compatible with Virtuoso’s import format
  - Load into Virtuoso’s user slots and assign to the virtualization engine

- If Virtuoso does not support user IR import:
  - Continue to use Impulcifer via Equalizer APO (see `HeSuVi_Installation_Guide.md`, Step 9B) for personalized HRTF processing on the `VoiceMeeter Input` device
  - Use Virtuoso only with its built-in HRTF profiles when comparing quality vs. the personalized chain

Tip: A/B by switching the active endpoint (Virtuoso output vs. E‑APO/Impulcifer include), not by stacking processors.

---

## Validation checklist
- [ ] Kodi shows `PCM 8‑ch @48 kHz`
- [ ] Virtuoso input meters show 8 channels, output is 2‑ch stereo
- [ ] Strong externalization and stable imaging on the horizontal plane
- [ ] Elevation is perceptible but not “true heights” (expected with bed‑only input)
- [ ] Lip‑sync aligned after Kodi Audio offset adjustment

Advanced (if you have a test generator)
- [ ] Discrete height test channels (e.g., Top Front L/R) mapped and audible above when fed as PCM

---

## Known limitations & alternatives
- No object rendering: Virtuoso does not decode Atmos objects. Only Dolby Access/AVR can render object metadata.
- No discrete heights in this path: Kodi/LAV → PCM is 7.1 bed only; Windows media pipelines generally cap at 8 PCM channels.

Alternatives
- Dolby Access (Windows Spatial Audio): full object rendering to binaural (generic HRTF; no personalization)
- Equalizer APO + Impulcifer: personalized HRTF with 7.1 bed; best individualization without objects
- External AVR: bitstream Atmos to an AVR for full object rendering to speakers (headphone path requires additional hardware/processing)

---

## Troubleshooting
- No signal in Virtuoso: verify input device selection and that VoiceMeeter is actually feeding the chosen ASIO device
- Channels scrambled: check channel mapping; ensure Lb/Rb not swapped with Ls/Rs
- Clipping/distortion: reduce preamp; confirm all devices run 48 kHz; increase buffer size
- Double audio or comb filtering: mute VoiceMeeter direct A1 when monitoring Virtuoso’s output
- Latency too high: try smaller buffers; ensure no extra processing chains are active (no double-virtualization)

---

## Next steps
- Evaluate Virtuoso’s spatial quality vs. E‑APO/Impulcifer. If Virtuoso cannot import user HRIRs and its elevation from bed content isn’t sufficient, stick with the personalized Impulcifer path or test Dolby Access for true object rendering.
