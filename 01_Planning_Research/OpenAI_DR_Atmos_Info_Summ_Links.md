Got it. Here’s a **linked** version you can copy/paste with working sources. I tightened a few bits so it’s easier to scan but kept the meat.

---

# Dolby Atmos Object Metadata Extraction for DIY HTPC Binaural Audio (Linked Edition)

## Why this is hard (but not impossible)

* **Atmos isn’t just channels**: Home Atmos carries a 7.1.2 *bed* plus up to **118 dynamic objects** (total inputs = 128). The object positions/size/trajectories are rendered at playback. ([Dolby Professional Support][1], [Sound Particles Blog][2])
* **Most PC pipelines drop objects**: Common software decoders (e.g., ffmpeg/LAV) historically extract only the TrueHD/DD+ *bed* and ignore Atmos object metadata; e.g., ffmpeg even documents filters that strip the Atmos extensions, and community maintainer threads confirm LAV has no open Atmos-object decode. ([ffmpeg.org][3], [trac.ffmpeg.org][4], [GitHub][5])
* **Windows stack reality**: Typical consumer Windows playback chains and drivers are built around **up to 7.1 PCM** (8 ch). You can bitstream Atmos to an AVR, but native >8ch PCM output paths are rare; forum and tool guidance repeatedly targets 5.1/7.1 for WASAPI. ([Audioholics Home Theater Forums][6], [AV NIRVANA][7], [Intel Community][8])

## What changed recently

* **Cavern (open-source) actually decodes Atmos**:

  * Cavern/Cavernize has long handled **DD+ Atmos (E-AC-3 JOC)** and converts it into arbitrary channel layouts. ([cavern.sbence.hu][9])
  * **TrueHD+Atmos (Blu-ray) support**: the project author announced/landed **TrueHD Atmos** decoding via a toolchain (`truehdd` ➜ DAMF ➜ WAV). This is offline (file conversion) rather than real-time, but it’s a first for PC without Dolby’s SDK. ([GitHub][10], [AVForums][11])
  * Project page & repo: overview and capabilities. ([GitHub][12], [cavern.sbence.hu][9])

* **Licensed route (studio tools)** still exists: Music Media Helper’s “Atmos Helper” drives **Dolby Reference Player** to spit out **7.1.4–9.1.6 WAVs/ADM** (but requires Dolby’s paid tooling). Community threads document 12–16ch WAV exports from TrueHD. ([QuadraphonicQuad Home Audio Forum][13], [AVS Forum][14])

## Can we render objects ourselves?

* **Yes, with open renderers**: The **EBU ADM Renderer (EAR)** is an open object renderer specified in **ITU-R BS.2127**; BBC/EBU’s **libear** (Apache-2.0) provides the math to render ADM objects to arbitrary layouts. You can pair it with HRTF convolution for headphones. ([GitHub][15], [Tech EBU][16])
* **How Dolby does headphone Atmos**: Dolby’s own binaural renderer applies an **HRTF per object** (position/size/binaural mode drive the filter selection). That exact closed algorithm isn’t public, but the approach is standard (per-object HRTF). ([Dolby Professional Support][17])

## Windows & Linux options to bypass the 8-channel wall

* **Windows Spatial Audio API**: You can feed **IAudio/ISpatialAudioClient** with object streams and let Windows Sonic/Dolby/DTS render them—but you **can’t inject your own HRTF** there (you’re stuck with the provider’s generic HRTF). Useful to understand, not ideal for personalized HRTF. ([Microsoft Learn][18])
* **Offline wins today**: Decode Atmos **offline** to a denser channel layout (e.g., **7.1.4**), then **binauralize** those channels with your **personal HRTF** (Impulcifer/APL Virtuoso/Reaper/FFmpeg+SOFA). During playback it’s just stereo, so Windows limitations disappear. ([cavern.sbence.hu][9])

## Practical, buildable workflow (local rips first)

1. **Demux the Atmos track**

   * Rip with MakeMKV; extract TrueHD/Atmos (`.thd`) or DD+ Atmos (`.ec3`). (Any demuxer works; example commandlines are in the community posts.) ([AVS Forum][14])

2. **Decode/“flatten” objects to a virtual speaker layout (offline)**

   * **Cavernize** the track to **7.1.4 (or 9.1.6) WAV/FLAC**. For TrueHD, the current flow is `truehdd → DAMF → WAV`. For DD+ Atmos, Cavernize works directly. ([GitHub][10], [cavern.sbence.hu][9])
   * Alt (licensed): **Dolby Reference Player** via Music Media Helper for **12–16ch WAV/ADM** exports. ([QuadraphonicQuad Home Audio Forum][13], [AVS Forum][14])

3. **Binaural render with your HRTF**

   * **APL Virtuoso**: feed the 7.1.4 program into Virtuoso configured with your **Impulcifer** HRTFs; output stereo.
   * **DAW/FFmpeg**: convolve each channel with the matching **HRTF IR** (SOFA/IR pairs), sum to L/R, export stereo WAV/FLAC. (SOFAlizer/afir in ffmpeg or Reaper+convolver).
   * This mimics Dolby’s per-object HRTF idea, but using **virtual speakers as proxies**, which is vastly better than “height collapsed to two channels” in 7.1 beds. ([Dolby Professional Support][17])

4. **Mux back & play**

   * Mux the **binaural stereo** into your MKV (label it “Headphone Atmos (binaural, personal HRTF)”). Playback is trivial on any OS—just select that track.

### Why 7.1.4 “virtual speakers” first?

Full per-object HRTF (convolution per object) in real-time is heavy and complex; a 7.1.4 (or 9.1.6) intermediate captures nearly all audible height/front-rear distinction and is **CPU-cheap** to convolve (12–16 channels vs. potentially dozens of objects). It’s the sweet spot today. (The community consensus also notes home Atmos often authors to 7.1.4-style layouts, with objects used selectively.) ([AVS Forum][19])

## What about **streaming Atmos**?

If you can legally obtain the **E-AC-3 JOC** bitstreams, **Cavern already supports DD+ Atmos** → convert as above. Quality is lossy vs TrueHD, but the object cues remain. ([cavern.sbence.hu][9])

## Real-time prospects & performance

* **Today**: treat it as **offline** (batch convert, then play). Zero playback latency; Windows channel limits don’t matter.
* **Future**: Cavern’s author is actively iterating; true real-time for TrueHD has been discussed, with the offline path already live. ([GitHub][10], [AVForums][11])
* **DIY real-time** would mean: TrueHD decode + many HRTF convolutions. Feasible on high-end CPUs with partitioned FFT, but not turnkey yet (and you still need player sync).

## Legal & licensing notes (plain language)

* Atmos encoding/decoding is **patented & proprietary**. Open implementations (like Cavern) are **reverse-engineered** and unlicensed by Dolby; typically fine for **personal use** but obviously not “Dolby-certified.” Using Dolby’s Reference Player requires a license. (Community threads around MMH/DRP are clear about that.) ([QuadraphonicQuad Home Audio Forum][13])

---

## TL;DR Implementation Roadmap (actionable)

1. **Pick a test clip** (short Atmos TrueHD scene).
2. **Demux** the `.thd`/`.ec3`. ([AVS Forum][14])
3. **Cavernize** to **7.1.4 WAV** (TrueHD: `truehdd → DAMF → WAV`). ([GitHub][10])
4. **Binauralize** with your HRTF (Virtuoso or DAW/ffmpeg+SOFA). ([Dolby Professional Support][17])
5. **Mux stereo track** back into MKV and **play**.
6. Iterate gains/EQ if needed (LFE routing, overhead balance).

---

## Handy links

* Dolby Atmos: objects vs beds, counts, 7.1.2 bed definition. ([Dolby Professional Support][1])
* Cavern project (overview + repo) and **TrueHD path**. ([cavern.sbence.hu][9], [GitHub][12])
* Community confirmations of **TrueHD → 12–16ch WAV** via DRP/MMH. ([AVS Forum][14], [QuadraphonicQuad Home Audio Forum][13])
* Open **object renderer** (EBU libear / ITU-R BS.2127). ([GitHub][15], [Tech EBU][16])
* Windows **Spatial Audio** API (for context). ([Microsoft Learn][20])
* Dolby doc on **per-object HRTF** in binaural rendering. ([Dolby Professional Support][17])

---

If you want, I can also generate a **clean Markdown doc** (or a PDF) with all these links embedded for your notes.

[1]: https://professionalsupport.dolby.com/s/article/What-is-an-Object-Bed-and-how-do-I-set-it-up?utm_source=chatgpt.com "What is an Object Bed and how do I set it up"
[2]: https://blog.soundparticles.com/what-is-object-based-audio?utm_source=chatgpt.com "What is Object-based Audio? - Sound Particles"
[3]: https://ffmpeg.org/ffmpeg-bitstream-filters.html?utm_source=chatgpt.com "FFmpeg Bitstream Filters Documentation"
[4]: https://trac.ffmpeg.org/ticket/7554?utm_source=chatgpt.com "#7554 (truehd_core bitstream filter to remove Atmos?) – FFmpeg"
[5]: https://github.com/Nevcairiel/LAVFilters/issues/344?utm_source=chatgpt.com "Spatial Audio · Issue #344 · Nevcairiel/LAVFilters · GitHub"
[6]: https://forums.audioholics.com/forums/threads/basic-set-up-with-rew-drivers-and-software-configuration.128325/?utm_source=chatgpt.com "Basic Set Up with REW, Drivers, and Software Configuration"
[7]: https://www.avnirvana.com/threads/rew-and-5-1-or-7-1-channel-multichannel-support-on-windows-10.6727/?utm_source=chatgpt.com "REW and 5.1 or 7.1 channel (multichannel) support on Windows 10"
[8]: https://community.intel.com/t5/Graphics/Windows-HDMI-Audio-Driver-WASAPI-PCM-4-0-FL-FR-SL-SR-layout/m-p/1316560?utm_source=chatgpt.com "Re:Windows HDMI Audio Driver - WASAPI PCM 4.0 FL+FR+SL+SR layout ..."
[9]: https://cavern.sbence.hu/cavern/?utm_source=chatgpt.com "Cavern"
[10]: https://github.com/VoidXH/Cavern/issues/241?utm_source=chatgpt.com "TrueHD · Issue #241 · VoidXH/Cavern - GitHub"
[11]: https://www.avforums.com/threads/atmos-decoding-on-a-pc.2534199/?utm_source=chatgpt.com "Atmos decoding on a PC - AVForums"
[12]: https://github.com/VoidXH/Cavern?utm_source=chatgpt.com "GitHub - VoidXH/Cavern: Object-based audio engine and codec pack with ..."
[13]: https://www.quadraphonicquad.com/forums/threads/mmh-new-atmos-decoder-beta-discussion.33488/page-13?utm_source=chatgpt.com "MMH - New Atmos Decoder (beta) discussion | Page 13 | QuadraphonicQuad ..."
[14]: https://www.avsforum.com/threads/decoding-truehd-atmos-to-16-channel-wav.3265364/?utm_source=chatgpt.com "Decoding TrueHD/Atmos to 16 channel WAV - AVS Forum"
[15]: https://github.com/ebu/libear?utm_source=chatgpt.com "GitHub - ebu/libear: A C++ library to render ADM content according to ..."
[16]: https://tech.ebu.ch/news/2019/09/easy-nga-implementations-with-c-library-from-bbc-and-irt?utm_source=chatgpt.com "Easy NGA implementations with C++ library from BBC and IRT | EBU ..."
[17]: https://professionalsupport.dolby.com/s/article/Why-should-I-mix-with-dynamic-objects-when-I-can-use-7-1-4-or-9-1-6-tracks?language=en_US&utm_source=chatgpt.com "Why should I mix with dynamic objects when I can use 7.1.4 or 9.1.6 tracks?"
[18]: https://learn.microsoft.com/en-us/windows/win32/coreaudio/render-spatial-sound-using-spatial-audio-objects?utm_source=chatgpt.com "Render Spatial Sound Using Spatial Audio Objects - Win32 apps"
[19]: https://www.avsforum.com/threads/does-atmos-for-home-really-have-a-7-channel-bed.3220715/?utm_source=chatgpt.com "Does Atmos for home really have a 7 channel bed? - AVS Forum"
[20]: https://learn.microsoft.com/en-us/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient?utm_source=chatgpt.com "ISpatialAudioClient (spatialaudioclient.h) - Win32 apps | Microsoft Learn"
