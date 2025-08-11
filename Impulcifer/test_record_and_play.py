import sounddevice as sd
import soundfile as sf
import numpy as np
from threading import Thread
from datetime import datetime

def record_audio(duration, fs, channels):
    print("Recording started...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, blocking=True)
    print("Recording finished")
    return recording

# Load the sweep file
sweep_file = "data/sweep-6.25s-48000Hz-16bit-39.06Hz-20000Hz.wav"
sweep_data, sweep_fs = sf.read(sweep_file)

# Create unique filename with timestamp
timestamp = datetime.now().strftime("%H%M%S")
output_file = f'data/test/voice_and_sweep_{timestamp}.wav'

print(f"Starting 10 second test... (Output: {output_file})")

# Start recording thread
record_thread = Thread(target=lambda: setattr(record_thread, 'result', 
                      record_audio(10, 48000, 2)))
record_thread.start()

# Play the sweep
print("Playing sweep...")
sd.play(sweep_data, sweep_fs, blocking=True)
print("Sweep complete")

# Wait for recording to finish
record_thread.join()
recording = record_thread.result

# Save the recording
sf.write(output_file, recording, 48000)
print(f"Saved to {output_file}")

# Print stats
max_amplitude = np.max(np.abs(recording))
if max_amplitude > 0:
    max_gain = 20 * np.log10(max_amplitude)
    print(f"Headroom: {0 - max_gain:.1f} dB")
    
    # Check for potential clipping
    if max_amplitude > 0.95:  # Allow some headroom before 1.0
        print("WARNING: Possible clipping detected!")
else:
    print("WARNING: No audio recorded (silent)")