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

# Load the voice test file
voice_file = "data/test/voice_test.wav"
voice_data, voice_fs = sf.read(voice_file)

# Create unique filename with timestamp
timestamp = datetime.now().strftime("%H%M%S")
output_file = f'data/test/rerecorded_voice_{timestamp}.wav'

print(f"Starting test... (Output: {output_file})")
print("Will play back your voice recording while recording")

# Start recording thread
record_thread = Thread(target=lambda: setattr(record_thread, 'result', 
                      record_audio(10, 48000, 2)))
record_thread.start()

# Play the voice recording
print("Playing voice recording...")
sd.play(voice_data, voice_fs, blocking=True)
print("Playback complete")

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
