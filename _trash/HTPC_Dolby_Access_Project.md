# HTPC + Dolby Access Project Plan
**Last Updated:** January 2025

---
## 🎯 Primary Objective
Build an ​HTPC-only playback chain that delivers a first-class Dolby Atmos headphone experience **without** an external AVR/processor.

Success means:
1. Kodi (or another Windows player) plays lossless Atmos content.
2. Dolby Access “Atmos for Headphones” performs object-based decoding & binaural rendering.
3. Output reaches the USB DAC/headphone amp with minimal latency & bit-depth loss.
4. Subjective listening tests show no obvious spatial limitations vs. a full AVR decode.

---
## ✅ Current Progress Snapshot
| Item | Status | Notes |
|------|--------|-------|
| Windows 11 Dolby Access installed & licensed | Pending | 15-day trial available. |
| Kodi bit-streaming (TrueHD/Atmos) verified | Working (8 ch bed) | WASAPI Exclusive path confirmed. |
| Default audio endpoint set to **“Dolby Atmos for Headphones”** | Pending | Must select in Windows Sound ► Spatial Audio. |
| USB DAC recognised at 24-bit/48 kHz | Working | Using Topping L50 chain. |
| Headphone listening test (Dolby Access demo) | Not done | Need subjective check. |

---
## 🔊 End-to-End Audio Signal Path
```text
(1) Kodi  ──►  (2) WASAPI Exclusive Stream (Bit-perfect 48 kHz TrueHD/Atmos)
          └─◄────────────── handshake / EDID reports "Atmos capable"
                        │
                        ▼
(3) Windows Spatial Audio Engine  ──► (4) Dolby Access Renderer Plug-in
                        │        • Mode A:  Atmos for Headphones  → 2-ch binaural PCM
                        │        • Mode B:  Atmos for Home Theater → 8-ch MAT 2.0 container
                        ▼
(5) System Mixer (disabled in Exclusive mode) ──► (6) WASAPI to USB DAC
                        ▼
                 Headphones via Topping L50
```

---
## 🧩 Component Technology Breakdown
### 1. Kodi (v20/21 “Omega”)
* Uses **FFmpeg + LAV Filters** for container parsing.
* In **WASAPI Exclusive / Passthrough** mode Kodi sends the raw Dolby TrueHD/Atmos bit-stream to the OS _unchanged_.
* EDID from the selected Windows audio endpoint must advertise Atmos capability or Kodi will refuse to bit-stream.

### 2. Windows Audio Stack
* **WASAPI Exclusive** guarantees bit-perfect delivery to the endpoint (no SRC/mixer).
* Endpoint is exposed by Dolby Access as either:
  - “Dolby Atmos for Home Theater” (8-ch LPCM container carrying MAT 2.0)
  - “Dolby Atmos for Headphones” (2-ch stereo endpoint)

### 3. Dolby Access Plug-in
* Acts as a licensing wrapper **and** a renderer.
* **Home Theater mode**: packages objects + metadata into MAT 2.0 (looks like 8-ch LPCM, 48 kHz, 32-bit).
* **Headphones mode**: renders full Atmos mix down to **binaural stereo** using proprietary HRTFs.
* Zero-latency; processed inside Windows Spatial Audio engine.

### 4. USB DAC / Headphone Chain
* Receives 2-channel 48 kHz PCM from Windows when in Headphones mode.
* No Dolby decoder needed downstream.

---
## ⚠️ Potential Issues & Unknowns
1. **Content DRM** – HDCP-protected UHD Blu-ray rips may fail to bit-stream; investigate MakeMKV → MKV **vs** ISO mounting.
2. **Sampling Rate Mismatch** – Atmos core is fixed @ 48 kHz; verify DAC stays in native rate to avoid SRC.
3. **Game Audio vs. Video Playback** – Windows Spatial Audio can only run one renderer per endpoint; test for conflicts.
4. **Subjective Quality** – Compare Dolby’s binaural result with HeSuVi/Virtuoso on identical content.
5. **Latency** – Measure round-trip latency; ensure lip-sync within ±50 ms.

---
## 🔜 Next Steps / Action Items
1. **Install & activate Dolby Access trial** on the HTPC.
2. **Set default output device** to “Dolby Atmos for Headphones”.
3. **Enable Passthrough in Kodi** for TrueHD/Atmos, test demo trailers.
4. **Listen & subjectively score** spatial immersion vs. stereo baseline.
5. **Capture bit-perfect verification** using WASAPI loopback & Audacity.
6. If satisfied, **purchase full Dolby Access license** (~$15). If not, move to Option 2.

---
## 📌 Decision Gate
If Dolby Access binaural quality ≥ Virtuoso & routing is stable, **project can finish here** – external AVR no longer required.

If quality is insufficient → Proceed to **Option 2** plan (VoiceMeeter + custom binaural).
