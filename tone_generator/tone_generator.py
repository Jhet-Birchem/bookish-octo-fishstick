from pydub import AudioSegment
from pydub.generators import Sine
import simpleaudio as sa

def play_tone(frequency, duration):
    """
    Generate and play a sine wave tone at the given frequency (in Hz) and duration (in milliseconds).
    """
    # Generate the sine wave tone
    tone = Sine(frequency).to_audio_segment(duration=duration)
    
    # Export to a raw audio format (WAV)
    raw_audio = tone.raw_data
    
    # Play the raw audio using simpleaudio
    play_obj = sa.play_buffer(raw_audio, num_channels=1, bytes_per_sample=2, sample_rate=44100)
    
    # Wait for playback to finish before exiting
    play_obj.wait_done()

if __name__ == "__main__":
    frequency = int(input("Enter the frequency (Hz): "))
    duration = int(input("Enter the duration (ms): "))
    
    play_tone(frequency, duration)