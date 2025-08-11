import sounddevice as sd
import soundfile as sf
import numpy as np

print("Recording 10 seconds...")
recording = sd.rec(int(10 * 48000), samplerate=48000, channels=2, blocking=True)
print("Recording complete")

# Save the recording
sf.write('data/test/voice_test.wav', recording, 48000)
print("Saved to data/test/voice_test.wav")

# Print stats
max_amplitude = np.max(np.abs(recording))
if max_amplitude > 0:
    max_gain = 20 * np.log10(max_amplitude)
    print(f"Headroom: {0 - max_gain:.1f} dB")
else:
    print("WARNING: No audio recorded (silent)")
