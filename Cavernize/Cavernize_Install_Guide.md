Thanks for the clarification. I’ll compare Windows 11 and Ubuntu support for Cavern, especially for extracting object or channel audio from MKV rips with automation in mind. I’ll also investigate the known issue with Windows 11 22H2, look for CLI support or workarounds, and provide confirmed, step-by-step installation instructions for the best platform.

I’ll let you know as soon as the findings are ready.


# Installing and Using Cavernize on Windows 11 (and Considerations for Ubuntu)

## Choosing the Best OS for Cavernize

Cavernize is primarily designed for **Windows**. The official Cavern downloads provide a Windows installer and portable package – there is **no native Linux build** on the site. In fact, users have noted that *“Cavern is Windows only”*. While it’s theoretically possible to run it on Ubuntu via workarounds (Wine or .NET Core), this is not officially supported and can be complex. For a smooth, reliable experience (especially with command-line automation), **Windows 11 is the recommended platform**. Ubuntu would require running the Windows app under emulation, which is not ideal for our needs.

**Bottom line:** Use Windows for Cavernize. The remainder of the guide will focus on Windows 11 installation and usage (with notes on any Ubuntu/Linux possibilities if needed).

## Prerequisites on Windows 11

Before installing Cavernize on Windows, make sure your system meets these requirements:

* **.NET 6/7 Runtime:** Cavernize is built in C#/.NET, so you need the appropriate .NET runtime installed. On **Windows 10**, install the **.NET 6** desktop runtime; on **Windows 11**, you can use **.NET 6 or .NET 7** (Windows 11 supports the newer .NET 7 as well). If the required .NET runtime is missing, the Cavernize app will fail to launch or exit immediately. You can download the .NET runtime from Microsoft’s website and run the installer. (If you use the Cavernize **installer** instead of the portable version, it may bundle or prompt for .NET – but it’s safest to install .NET yourself first.)
* **FFmpeg (optional):** Cavernize can perform most conversions internally, but certain output formats use FFmpeg in the background. If you plan to output to formats like AC-3 or E-AC-3 (Dolby Digital), or other cases where Cavern isn’t fully self-sufficient, having FFmpeg installed is helpful. You can download a static build of FFmpeg, unzip it, and either add it to your PATH or note its location. Cavernize will auto-detect FFmpeg if it’s in PATH and show a “Ready!” status in the UI. *(For simple PCM/FLAC outputs to MKV, FFmpeg isn’t required.)*
* **Audio Drivers Updated (General OS note):** Ensure your Windows 11 audio drivers are up to date. There have been instances of **audio issues after the Windows 11 22H2 update** (e.g. Realtek sound stopping until drivers are reinstalled). This isn’t directly a Cavernize issue, but to avoid confusion, confirm that your system audio is working normally. If you recently updated Windows and lost sound, reinstalling the audio driver or running the audio troubleshooter can resolve it.

## Step-by-Step: Installing Cavernize on Windows 11

Follow these steps to install Cavernize 2.0.2 on your Windows 11 machine. We’ll cover both the installer method and the portable (no installer) method:

1. **Download Cavernize:** Visit the official Cavern downloads page and download **Cavernize 2.0.2** for Windows. There are two options: a standard installer (`.exe`) and a portable zip package. For most users, the **installer** is easiest (it may ensure dependencies are in place). The **portable** version is a ZIP archive if you prefer no installation.

   * *Installer:* Click “Download for Windows” on the Cavernize section and save the `.exe` file.
   * *Portable:* Click “Download portable (Windows)” to get the ZIP file.

2. **Run the Installer (if using .exe):** Locate the downloaded `Cavernize_2.0.2_setup.exe` (for example) and double-click it. If Windows SmartScreen prompts “unknown publisher”, click **“More info”** then **“Run anyway”** – Cavernize is a trusted open-source tool. Follow the installation wizard prompts to install Cavernize. By default it may install to `C:\Program Files\Cavern` or a location you choose. Once finished, skip to step 4. (The installer should also install the required .NET runtime if it’s not present, or prompt you to download it.)

3. **Extract the Portable (if using ZIP):** If you chose the portable download, right-click the `Cavernize_2.0.2.zip` file and select **“Extract All…”**. Choose a destination folder (for example, `C:\Apps\Cavernize`) and extract the contents. You can also open the ZIP and drag out the folder. After extraction, you should have a folder containing files like `CavernizeGUI.exe` and related DLLs. *Note:* If you open the ZIP without extracting, Windows may show a security warning when launching the app – it’s recommended to fully extract it first.

4. **Install .NET if Needed:** If you haven’t already, install the .NET runtime **before** launching Cavernize. Windows 11 users can install **.NET 7 Runtime** (Desktop) which covers .NET 6 apps as well, or specifically install **.NET 6 Runtime** (LTS). Having .NET 6/7 in place is crucial. You can verify .NET is installed by running “Apps > App Execution Aliases” or simply running the Cavernize app to see if it complains. (If the Cavernize installer was used, this step might not be necessary if it bundled the runtime.)

5. **Launch Cavernize:** Now start the application:

   * *If installed:* Find **Cavernize** in your Start Menu (or on your desktop, if a shortcut was added) and launch it.
   * *If portable:* Navigate to the extracted folder and double-click `CavernizeGUI.exe` (the icon with a “C”). This will open the Cavernize GUI application.
     The first launch might take a moment as it initializes. You should see the Cavernize interface with options to select channel layout, input file, etc. If the app **does not open at all** or closes instantly, this typically means the .NET runtime was not found – double-check that .NET 6 or 7 is installed in Windows. If SmartScreen blocked it, use the “Run anyway” as mentioned.

6. **Verify the Version:** In the Cavernize GUI, go to **Help > About** or check the title bar to ensure it’s version 2.0.2 (the latest as of July 2025). This version supports both Dolby Digital Plus Atmos (E-AC-3 JOC) and Dolby TrueHD Atmos decoding. Using the latest version is important – older versions had limitations (for example, early releases in 2022 could not fully decode TrueHD Atmos content). Version 2.x should handle TrueHD tracks via an integrated `truehdd` decoder.

7. **(Optional) Configure FFmpeg:** If you plan to output to certain formats that require FFmpeg (e.g. encoding to AC-3), ensure Cavernize recognizes FFmpeg. If FFmpeg is in your PATH, Cavernize will show a “Ready!” message at the bottom of the window indicating it found it. If not, you can click a “Locate FFmpeg” button in Cavernize’s settings and browse to the `ffmpeg.exe`. For basic PCM/FLAC outputs, you can skip this – Cavernize can render those internally without external tools.

At this point, Cavernize is installed and ready on Windows 11. You can use the graphical interface to set up your speaker layout, open an MKV with an Atmos track, and render it to a new audio file (as per the Cavern documentation’s quick guide). But since you mentioned automation and CLI usage, we’ll cover the console mode next.

## Using Cavernize via Command-Line (CLI Mode)

One of Cavernize’s strengths is that it can be driven from the **command line**, allowing batch processing and automation (no GUI clicks). The Cavernize application supports various command-line arguments to specify the input, output, and conversion settings. This means you can write scripts to extract audio from many MKVs in a folder, for example, without manual intervention.

**Key CLI arguments:** (you can view all by running `CavernizeGUI.exe -h`)

* `-i` or `-input` – **Input file.** Specifies the path to the source file (e.g. an `.mkv` or `.mka` with an Atmos track). If this is the first argument, Cavernize will load that file on startup.
* `-t` or `-target` – **Target layout.** Sets the desired channel layout for output. You can use common notation; for example, `"5.1.2"` (or even `"512"`) for a 7.1-channel layout with 2 height channels (5 bed + 1 LFE + 2 heights). Cavernize supports standard layouts up to 7.1.4 and even custom layouts (via Cavern Driver or headphone virtualization) if you have more channels. **Example:** `-t 5.1.2` or `-t "7.1.4"` (quotes may be needed in some shells because of dots).
* `-f` or `-format` – **Output audio codec/format.** Chooses the format for the rendered audio track. Valid options include: `FLAC` (lossless FLAC), `PCM_LE` (PCM little-endian integer), `PCM_Float` (32-bit float PCM), `Opus` (Opus audio), `ADM_BWF` (ADM Broadcast WAV for up to 128 channels), `ADM_BWF_Atmos` (ADM WAV with Atmos metadata), `LimitlessAudio` (the custom .laf format), etc. For most use cases, **FLAC** or **PCM** are good choices (FLAC is compressed lossless but limited to 8 channels; PCM is uncompressed and can handle many channels in an MKV or WAV).
* `-o` or `-output` – **Output file path.** Specifies the filename (and format) for the rendered output. The extension and format should match the `-format` chosen. For example, if you choose `-f FLAC`, you might output to `output.mkv` (which will contain a FLAC track) or `output.flac`. If you choose `PCM_LE` you might output to a `.wav` or `.mka` container. *(Cavernize can embed audio in an MKV container directly – e.g. a multichannel FLAC or PCM track inside an .mkv – which is useful for preserving video, but you can also create audio-only files.)*

There are additional arguments for fine control – for instance, `-mb` (mute bed channels), `-mg` (mute ground-level objects), or upmixing toggles (`-mx`, `-u`) – but these are advanced tweaks. For basic extraction of channel-based audio, the main ones above are sufficient.

**Example CLI usage:** Suppose you want to convert an Atmos MKV to a 7.1.4 channel WAV file. You could run:

```batch
CavernizeGUI.exe -i "MovieAtmos.mkv" -t 7.1.4 -f PCM_LE -o "MovieAtmos_7.1.4.wav"
```

This will launch Cavernize in console mode, load *MovieAtmos.mkv*, render the audio into a 7.1.4 layout, and save it as *MovieAtmos\_7.1.4.wav*. No GUI interaction needed – you’ll see progress in the console or it will simply produce the file. If you prefer FLAC and your layout is 5.1.2 or fewer (8 channels max), you could do:

```batch
CavernizeGUI.exe -i "ShowAtmos.mkv" -t 5.1.2 -f FLAC -o "ShowAtmos_5.1.2.mkv"
```

This would output a `.mkv` file containing a 5.1.2 FLAC audio track (suitable for playback on any 7.1-capable system). Cavernize will remember your last GUI settings for anything not specified via CLI, but you can override any setting with arguments. For a full list of command options, run `CavernizeGUI.exe -help` – it will list all available commands and their descriptions.

**Batch processing:** You can call these commands from a PowerShell or batch script and loop over multiple files. As of late 2022, the developer added support for processing entire folders in one go (and the GUI queue feature), so you can script conversions easily. This is ideal for automating object/channel audio extraction from a batch of MKVs.

## Common Issues and Workarounds

Even with proper installation, you might encounter a few hiccups. Here are known issues people have run into with Cavernize and how to address them:

* **Application won’t launch (Windows 11):** If you double-click Cavernize and nothing happens, or a window flashes and closes, the most likely cause is a missing .NET runtime. Ensure you’ve installed **.NET 6 or 7** on Windows 11. You can download the “Desktop Runtime” from Microsoft’s site and install it, then try launching Cavernize again. If it’s still not launching, run `CavernizeGUI.exe` from a Command Prompt to see any error output. Also verify the files extracted correctly (re-extract if in doubt). Running the latest Windows updates doesn’t hurt either, as .NET fixes may come through Windows Update. *(Note: This issue is specific to the app not starting. It’s separate from the general Windows 11 22H2 audio-driver bug which could mute system sound – that doesn’t stop the app from running.)*

* **SmartScreen or Antivirus blocking:** Because Cavernize is a niche tool, Windows SmartScreen might flag it simply because it’s not widely recognized. If you downloaded from the official site, it’s safe. Click “More info” and “Run anyway” on the SmartScreen prompt. If your antivirus is blocking or sandboxing it, you may need to whitelist the Cavernize folder.

* **TrueHD Atmos decoding issues:** Cavernize 2.x supports TrueHD Atmos tracks (from Blu-rays, for example) as well as E-AC-3 Atmos (from streaming sources). If you find that a TrueHD track isn’t being processed or only the base 7.1 audio comes out, double-check that you’re using the latest version. Early Cavernize versions (circa 2022) did **not** handle TrueHD Atmos, but as of Cavern 2.0+ this is implemented (via the `truehdd` decoder). Always use the newest release for full codec support.

* **Output file has no sound or missing channels:** If the resulting file is completely silent or some channels seem empty, consider a few things:

  * **Channel count limits:** Standard PC audio devices and some media players can’t handle more than 8 channels. Cavernize will happily create a 10 or 12-channel WAV, but playing that on a normal setup may result in silence (because Windows DirectSound is limited to 8 channels output). For example, *MPC-HC* will not play audio if the track has more than 8 channels (it simply fails to play it). In such cases, try using **VLC** (which can downmix or handle more channels in software) or output to a maximum of 8 channels (7.1 or 5.1.2) for compatibility. If you truly need to render all objects into discrete channels beyond 7.1, consider using the **ADM BWF** or **Limitless Audio Format** outputs which support large channel counts, and be prepared to use professional audio tools or players that support those.
  * **Player channel mapping issues:** Some players don’t respect the standard channel order in multichannel WAV/FLAC files. Cavernize exports channels with the standard WAVE channel order (L, R, C, LFE, RL, RR, SL, SR for 7.1) and tags this in metadata. However, **VLC** and certain hardware media players ignore that metadata and assume a different channel order, causing misrouted sound. For instance, VLC’s default 7.1 order is L, R, SL, SR, RL, RR, C, LFE which will make dialog and effects play from wrong speakers. The workaround is to use a player that respects channel order (MPC-HC is verified to play Cavernize outputs correctly) or choose an output format that inherently carries channel mapping (e.g., an **AC-3/EAC-3** track, although lossy, or an **ADM BWF** which is a professional format). If using VLC, you might stick to 5.1 output (which is unambiguous) or use a custom channel remapping filter in VLC.
  * **Bed channels vs object channels:** If you hear too much of certain channels, you might experiment with Cavernize’s options like **`-mb`** (mute bed) or **`-mg`** (mute ground objects) which can isolate certain elements. This is more for advanced “auditioning” of object vs bed content. Normally, you’d keep all channels on.

* \*\*“Audio cuts out” or **A/V sync issues in output:** This primarily applies when playing back the converted file:

  * If the audio periodically goes silent or the video stutters, and **if you used an MXF container** (ADM BWF) or certain complex formats, it’s known that *MPC-HC* might lose sync or drop audio due to how it handles those tracks. Oddly, in these cases **VLC** plays them fine. The Cavern documentation notes this for MXF/ADM outputs. If you encounter this, one solution is to demux video and audio into separate files (e.g., play the video in one file and audio in another) or use a different player. The Cavern docs provide a sample FFmpeg batch snippet to split the video and audio streams to avoid MPC’s issue. But if you’re sticking to standard MKV+FLAC/PCM outputs, you shouldn’t see this problem.
  * If Cavernize itself gave an **error message during conversion** (e.g., “contains something Cavernize can’t decode”), then that portion of audio was muted in the output. This could happen if the Atmos track has an unsupported feature (perhaps very rare metadata). In such cases, there may not be a fix (it’s a limitation of the current decoder). Ensure you didn’t miss any dependency. If it’s a reproducible bug, consider reporting it to the developer.

* **Conversion fails or crashes:** If Cavernize crashes or throws unexplained errors partway through a render, check the simplest things first: **disk space** and **FFmpeg status**. A common cause is the target drive running out of space (uncompressed audio files, especially WAV, can be huge). Also, if Cavernize needed FFmpeg and it was closed or blocked, the process can fail. Free up disk space and try again. If it still crashes on a specific file, it could be a bug – use the Cavern contact form to report it, or try a different output format as a test.

## Notes on Ubuntu/Linux Usage (if attempted)

While we strongly recommend Windows for Cavernize, for completeness here are notes if you **must** try it on Ubuntu:

* **Wine/Proton:** Some users have hypothesized running Cavernize under Wine. Since Cavernize is a .NET app, you would need to install **Wine Mono** or (preferably) use **winetricks** to install .NET 6 runtime in the Wine prefix. This can be non-trivial, and the GUI (which likely uses WPF) may not render properly in Wine. There is anecdotal mention of using *Hangover* (an ARM Wine variant) on a Raspberry Pi to run Cavern, but that’s an extreme case. On a standard x86\_64 Ubuntu, regular Wine might run the CLI portion. If you go this route, focus on using the CLI arguments (so you don’t rely on the GUI). Expect to spend time troubleshooting if it doesn’t work – again, this is not officially documented by the Cavern developers.
* **Native build via .NET:** The Cavern library itself is .NET Standard and open-source. In theory, one could compile a console application using the Cavern API on Linux (since .NET 6/7 are cross-platform) – but the provided Cavernize tool includes a Windows-only GUI front-end. If you are a developer, you could attempt to write a small .NET 7 console app that calls the Cavern API to decode an Atmos track. However, this is a deep DIY project and beyond typical usage. There is no ready-made CLI binary for Linux from the author.

In short, **Ubuntu can be used only with significant effort** and is not guaranteed. For automating your MKV audio extractions, a Windows environment (or even a Windows VM on your Linux box) is the far easier solution given Cavernize’s design.

## Conclusion

To summarize, **use Windows 11 (or 10) for Cavernize**, install the required .NET runtime, and follow the official instructions for setup. The installation is straightforward on Windows when prerequisites are met, and Cavernize offers both a user-friendly GUI and a powerful CLI mode for automation. We’ve addressed known pitfalls – from .NET issues on Win11 to channel mapping quirks – so you can avoid or work around them.

Cavernize is indeed a unique solution for converting object-based audio (Dolby Atmos) into channel-based audio files that “can then be played on practically anything”. By choosing the appropriate output format and layout for your needs, you can extract individual audio channels or downmix objects into standard surround channels as required. With the above setup and tips, you should be well-equipped to install Cavernize and integrate it into your automated workflow for MKV audio extraction. Enjoy your **object-based audio** extractions!

**Sources:**

* Cavern official documentation and downloads
* User forums and reports (AudioScienceReview, Chinese HT forums) confirming Windows-only support and .NET requirements
* Cavern troubleshooting guide (channel order, playback issues, etc.)
* Developer notes on CLI feature and batch conversion
* Microsoft/Community notes on Windows 11 22H2 audio driver issues
* Cavern feature list / supported formats (TrueHD, E-AC-3 Atmos support).
