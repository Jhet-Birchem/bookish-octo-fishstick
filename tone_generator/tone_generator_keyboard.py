import tkinter as tk
from tkinter import ttk
from pydub.generators import Sine
import simpleaudio as sa
import time

# Define piano keys (C4 to C5)
keys = [
    ("C4", 261.63),
    ("C#4", 277.18),
    ("D4", 293.66),
    ("D#4", 311.13),
    ("E4", 329.63),
    ("F4", 349.23),
    ("F#4", 369.99),
    ("G4", 392.00),
    ("G#4", 415.30),
    ("A4", 440.00),
    ("A#4", 466.16),
    ("B4", 493.88),
    ("C5", 523.25),
]

# Global variable to track the start time of a key press
start_time = None

# Function to play a tone
def play_tone(frequency, volume, duration):
    # Generate the sine wave tone
    sine_wave = Sine(frequency).to_audio_segment(duration=duration)
    
    # Adjust volume (volume range is 0 to 10)
    sine_wave = sine_wave + (volume - 5) * 6  # Adjust to a range that's safe for 16-bit audio
    
    # Export to a raw audio format (WAV)
    raw_audio = sine_wave.raw_data
    
    # Play the raw audio using simpleaudio
    play_obj = sa.play_buffer(raw_audio, num_channels=1, bytes_per_sample=2, sample_rate=44100)
    
    # Wait for playback to finish before exiting
    play_obj.wait_done()

# Function to handle key press
def key_pressed(event, frequency):
    global start_time
    start_time = time.time()

# Function to handle key release
def key_released(event, frequency, volume_slider):
    global start_time
    if start_time:
        duration = int((time.time() - start_time) * 1000)  # Duration in milliseconds
        volume = volume_slider.get()
        play_tone(frequency, volume, duration)
        start_time = None

# Create the main window
root = tk.Tk()
root.title("Simple Piano")

# Create a frame for the piano keys
piano_frame = tk.Frame(root)
piano_frame.pack(pady=20)

# Create a slider for volume control
volume_slider = ttk.Scale(root, from_=0, to=10, orient="horizontal", length=200)
volume_slider.set(5)  # Set initial volume to 5
volume_slider.pack(pady=10)
volume_label = tk.Label(root, text="Volume")
volume_label.pack()

# Create piano keys (buttons)
for idx, (note, freq) in enumerate(keys):
    btn = tk.Button(piano_frame, text=note, width=5, height=10)
    btn.grid(row=0, column=idx)
    
    # Bind key press and release events to each button
    btn.bind("<ButtonPress-1>", lambda event, freq=freq: key_pressed(event, freq))
    btn.bind("<ButtonRelease-1>", lambda event, freq=freq: key_released(event, freq, volume_slider))

# Run the main event loop
root.mainloop()
