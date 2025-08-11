#!/usr/bin/env python3
"""
Interactive HRTF Measurement Guide for 9.1.6
Guides user through all 16 measurements with prompts and positioning instructions
"""

import os
import subprocess
import sys
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_user():
    input("\nPress ENTER when ready to record...")

def run_recording(sweep_file, output_file, input_device=None, output_device=None):
    """Run the recording command"""
    # Resolve project base dir (directory of this script)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print("\n--- PRE-FLIGHT CHECKS ---")
    print(f"Base directory: {base_dir}")
    print(f"Sweep file:     {os.path.abspath(sweep_file)}")
    print(f"Output file:    {os.path.abspath(output_file)}")
    # Validate sweep file exists
    if not os.path.isfile(sweep_file):
        print(f"❌ ERROR: Sweep file not found: {sweep_file}")
        return False
    # Ensure output directory exists and is writable
    out_dir = os.path.dirname(os.path.abspath(output_file))
    try:
        os.makedirs(out_dir, exist_ok=True)
    except Exception as ex:
        print(f"❌ ERROR: Failed to create output directory '{out_dir}': {ex}")
        return False
    # Writeability test
    try:
        test_path = os.path.join(out_dir, ".__write_test__.tmp")
        with open(test_path, "wb") as fh:
            fh.write(b"OK")
        os.remove(test_path)
        print(f"✅ Output directory is writable: {out_dir}")
    except Exception as ex:
        print(f"❌ ERROR: No write permission to '{out_dir}': {ex}")
        return False
    
    # Use the virtual environment's Python executable
    python_exe = os.path.join(base_dir, "venv", "Scripts", "python.exe")
    if not os.path.exists(python_exe):
        python_exe = "python"  # Fallback to system python
        print("ℹ️  Using system Python from PATH")
    else:
        print(f"ℹ️  Using venv Python: {python_exe}")
    
    # Absolute path to recorder.py
    recorder_py = os.path.join(base_dir, "recorder.py")
    if not os.path.isfile(recorder_py):
        print(f"❌ ERROR: recorder.py not found at: {recorder_py}")
        return False
    
    # Build command with audio device options - force minimal requirements for basic setups
    cmd = (
        f'"{python_exe}" "{recorder_py}" '
        f'--play="{sweep_file}" --record="{output_file}" --channels=2 --host_api=MME'
    )
    
    # For basic audio setups, try to use default devices without specific requirements
    if input_device:
        cmd += f' --input_device="{input_device}"'
    else:
        print("Using default input device...")
        
    if output_device:
        cmd += f' --output_device="{output_device}"'
    else:
        print("Using default output device...")
    
    print(f"\n--- EXECUTION ---")
    print(f"Command: {cmd}")
    print(f"Recording will be saved to: {os.path.abspath(output_file)}")
    try:
        # Always run from project base directory so relative imports and paths resolve
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            cwd=base_dir,
            capture_output=True,
            text=True,
        )
        
        # Verify file was created and has content
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"✅ Recording completed successfully! File size: {file_size:,} bytes")
            if file_size <= 48:  # WAV header only = empty file
                print("⚠️  WARNING: File appears to be empty (only WAV header)")
        else:
            print("❌ ERROR: Recording file was not created!")
            return False
            
        if result.stdout:
            print("STDOUT:")
            print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Recording failed with exit code {e.returncode}")
        if e.stdout:
            print("STDOUT:")
            print(e.stdout)
        if e.stderr:
            print("STDERR:")
            print(e.stderr)
        print("\n" + "="*50)
        print("RECORDING ERROR - SCRIPT PAUSED")
        print("="*50)
        retry = input("Would you like to retry this measurement? (y/n): ")
        return retry.lower() == 'y'
    except KeyboardInterrupt:
        print("\n⚠️  Recording interrupted by user")
        return False

def main():
    # Configuration
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sweep_file = os.path.join(base_dir, "data", "sweep-6.03s-48000Hz-16bit-78.12Hz-20000Hz.wav")
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M")
    data_dir = os.path.join(base_dir, f"data/my_hrir_{timestamp}")
    
    # Create output directory
    os.makedirs(data_dir, exist_ok=True)
    
    print("=" * 70)
    print("🎧 INTERACTIVE HRTF MEASUREMENT GUIDE - 9.1.6 LAYOUT")
    print("=" * 70)
    print(f"Output directory: {data_dir}")
    print(f"Sweep file: {sweep_file}")
    print(f"Total measurements: 16 (1 headphone + 15 speaker positions)")
    print()
    
    # Audio device configuration
    print("AUDIO DEVICE SETUP:")
    print("Since you don't have a full 9.1.6 system available, we'll use:")
    print("• Default Windows audio devices")
    print("• Single-channel output (any speaker/headphones)")
    print("• Your USB binaural microphones for input")
    print()
    print("This approach will work with any basic audio setup.")
    print("You'll position yourself relative to a single speaker for each measurement.")
    print()
    
    use_defaults = input("Use default audio devices? (recommended: y/n): ").strip().lower()
    if use_defaults != 'y':
        input_device = input("Input device name (or press ENTER for default): ").strip()
        if not input_device:
            input_device = None
        
        output_device = input("Output device name (or press ENTER for default): ").strip()
        if not output_device:
            output_device = None
    else:
        input_device = None
        output_device = None
        print("✅ Using Windows default audio devices")
    
    print()
    print("IMPORTANT SETUP REMINDERS:")
    print("• Insert binaural microphones securely in ears")
    print("• Keep microphone insertion depth identical for all measurements")
    print("• Maintain head position (upright, eyes forward)")
    print("• Ensure quiet room environment")
    print("• Keep consistent speaker distance (1-1.5m)")
    print("• Using SINGLE SPEAKER: Position yourself for each virtual speaker location")
    
    input("\nPress ENTER to begin measurements...")
    
    # Define all measurements
    measurements = [
        {
            "name": "Headphone Compensation",
            "file": "headphones.wav",
            "position": "Sitting upright, looking forward",
            "setup": "• Binaural mics in ears\n• Put HEADPHONES ON over the microphones\n• No speaker positioning needed",
            "angle": "N/A (headphones)",
            "notes": "This captures headphone coloration to subtract from speaker measurements"
        },
        
        # BED CHANNELS (9.1)
        {
            "name": "Front Center",
            "file": "FC.wav", 
            "position": "Speaker at 0° azimuth, 0° elevation",
            "setup": "• Speaker directly in front of you\n• At ear height\n• Remove headphones, keep mics in ears",
            "angle": "0°, 0°",
            "notes": "Main dialogue channel - critical for center imaging"
        },
        {
            "name": "Front Left", 
            "file": "FL.wav",
            "position": "Speaker at -30° azimuth, 0° elevation", 
            "setup": "• Speaker 30° to your left\n• At ear height\n• Head facing forward (0°)",
            "angle": "-30°, 0°",
            "notes": "Primary left channel"
        },
        {
            "name": "Front Right",
            "file": "FR.wav", 
            "position": "Speaker at +30° azimuth, 0° elevation",
            "setup": "• Speaker 30° to your right\n• At ear height\n• Head facing forward (0°)", 
            "angle": "+30°, 0°",
            "notes": "Primary right channel"
        },
        {
            "name": "Wide Left",
            "file": "WL.wav",
            "position": "Speaker at -60° azimuth, 0° elevation",
            "setup": "• Speaker 60° to your left (between front and side)\n• At ear height\n• Head facing forward (0°)",
            "angle": "-60°, 0°", 
            "notes": "Wide stereo imaging"
        },
        {
            "name": "Wide Right",
            "file": "WR.wav",
            "position": "Speaker at +60° azimuth, 0° elevation", 
            "setup": "• Speaker 60° to your right (between front and side)\n• At ear height\n• Head facing forward (0°)",
            "angle": "+60°, 0°",
            "notes": "Wide stereo imaging"
        },
        {
            "name": "Side Left",
            "file": "SL.wav",
            "position": "Speaker at -90° azimuth, 0° elevation",
            "setup": "• Speaker directly to your left\n• At ear height\n• Head facing forward (0°)",
            "angle": "-90°, 0°", 
            "notes": "Primary surround left"
        },
        {
            "name": "Side Right", 
            "file": "SR.wav",
            "position": "Speaker at +90° azimuth, 0° elevation",
            "setup": "• Speaker directly to your right\n• At ear height\n• Head facing forward (0°)",
            "angle": "+90°, 0°",
            "notes": "Primary surround right"
        },
        {
            "name": "Back Left",
            "file": "BL.wav", 
            "position": "Speaker at -150° azimuth, 0° elevation",
            "setup": "• Speaker 150° to your left (behind you, left side)\n• At ear height\n• Head facing forward (0°)",
            "angle": "-150°, 0°",
            "notes": "Rear surround left"
        },
        {
            "name": "Back Right",
            "file": "BR.wav",
            "position": "Speaker at +150° azimuth, 0° elevation", 
            "setup": "• Speaker 150° to your right (behind you, right side)\n• At ear height\n• Head facing forward (0°)",
            "angle": "+150°, 0°",
            "notes": "Rear surround right" 
        },
        
        # HEIGHT CHANNELS (.6)
        {
            "name": "Top Front Left",
            "file": "TFL.wav",
            "position": "Speaker at -30° azimuth, +35° elevation", 
            "setup": "• Speaker 30° to your left, elevated 35° above ear level\n• Can elevate speaker or recline chair ~35°\n• Head facing forward (0°)",
            "angle": "-30°, +35°",
            "notes": "Primary height channel - crucial for overhead imaging"
        },
        {
            "name": "Top Front Right", 
            "file": "TFR.wav",
            "position": "Speaker at +30° azimuth, +35° elevation",
            "setup": "• Speaker 30° to your right, elevated 35° above ear level\n• Can elevate speaker or recline chair ~35°\n• Head facing forward (0°)", 
            "angle": "+30°, +35°",
            "notes": "Primary height channel - crucial for overhead imaging"
        },
        {
            "name": "Top Middle Left",
            "file": "TML.wav", 
            "position": "Speaker at -90° azimuth, +90° elevation",
            "setup": "• Speaker directly above your left ear\n• 90° elevation (straight up from side)\n• Most challenging position - be creative with mounting",
            "angle": "-90°, +90°",
            "notes": "Overhead side imaging for object-based audio"
        },
        {
            "name": "Top Middle Right",
            "file": "TMR.wav",
            "position": "Speaker at +90° azimuth, +90° elevation", 
            "setup": "• Speaker directly above your right ear\n• 90° elevation (straight up from side)\n• Most challenging position - be creative with mounting",
            "angle": "+90°, +90°",
            "notes": "Overhead side imaging for object-based audio"
        },
        {
            "name": "Top Back Left", 
            "file": "TBL.wav",
            "position": "Speaker at -150° azimuth, +35° elevation",
            "setup": "• Speaker 150° to your left (behind), elevated 35°\n• Can elevate speaker or recline chair ~35°\n• Head facing forward (0°)",
            "angle": "-150°, +35°",
            "notes": "Rear height channel"
        },
        {
            "name": "Top Back Right",
            "file": "TBR.wav", 
            "position": "Speaker at +150° azimuth, +35° elevation",
            "setup": "• Speaker 150° to your right (behind), elevated 35°\n• Can elevate speaker or recline chair ~35°\n• Head facing forward (0°)",
            "angle": "+150°, +35°", 
            "notes": "Rear height channel"
        }
    ]
    
    # Execute measurements
    for i, measurement in enumerate(measurements, 1):
        while True:  # Loop for retries
            clear_screen()
            print("=" * 70)
            print(f"MEASUREMENT {i}/16: {measurement['name'].upper()}")
            print("=" * 70)
            print(f"Position: {measurement['angle']}")
            print(f"Output file: {measurement['file']}")
            print()
            print("SETUP INSTRUCTIONS:")
            print(measurement['setup'])
            print()
            print("POSITIONING:")
            print(f"• {measurement['position']}")
            print()
            print("NOTES:")
            print(f"• {measurement['notes']}")
            print()
            print("REMINDERS:")
            print("• Keep microphone placement identical to previous measurements")
            print("• Maintain consistent speaker distance") 
            print("• Stay perfectly still during the 6.25-second sweep")
            print("• Ensure room is quiet (no HVAC, fans, etc.)")
            
            wait_for_user()
            
            output_path = os.path.join(data_dir, measurement['file'])
            success = run_recording(sweep_file, output_path, input_device, output_device)
            
            if success:
                break
            else:
                print("\nMeasurement failed or was interrupted.")
                choice = input("Choose: (r)etry, (s)kip, or (q)uit: ").lower()
                if choice == 's':
                    print(f"⚠️  Skipping {measurement['name']}")
                    break
                elif choice == 'q':
                    print("Measurement session terminated by user.")
                    return
                # 'r' or any other input will retry
    
    # Completion summary
    clear_screen()
    print("=" * 70)
    print("🎉 HRTF MEASUREMENTS COMPLETED!")
    print("=" * 70)
    print(f"All recordings saved to: {data_dir}")
    print()
    print("NEXT STEPS:")
    print("1. Process recordings with Impulcifer:")
    # Use the virtual environment's Python executable
    python_exe = os.path.join(base_dir, "venv", "Scripts", "python.exe")
    if not os.path.exists(python_exe):
        python_exe = "python"  # Fallback to system python
    print(f'   "{python_exe}" impulcifer.py --test_signal="{sweep_file}" --dir_path="{data_dir}" --fs=48000 --plot')
    print()
    print("2. The processing will generate:")
    print("   • hrir.wav - Your custom HRTF file")
    print("   • hesuvi.wav - Compatible with HeSuVi")
    print("   • Analysis plots (frequency response, etc.)")
    print()
    print("3. Copy hesuvi.wav to EqualizerAPO for use with your HTPC setup")
    print()
    print("Enjoy your personalized 9.1.6 spatial audio! 🎧✨")

if __name__ == "__main__":
    main()
