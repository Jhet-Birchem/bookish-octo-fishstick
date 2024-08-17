import tkinter as tk
from tkinter import ttk
import numpy as np
import simpleaudio as sa
import threading

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

# Global variables for playback control
playback_thread = None
stop_thread = threading.Event()

# Function to generate a sine wave
def generate_sine_wave(frequency, duration, volume):
    print(f"Generating sine wave: frequency={frequency}, duration={duration}, volume={volume}")
    sample_rate = 44100
    try:
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave_data = 0.5 * volume * np.sin(2 * np.pi * frequency * t)
        audio_data = np.int16(wave_data * 32767)
        print("Sine wave generated.")
    except Exception as e:
        print(f"Error during sine wave generation: {e}")
        raise e
    return audio_data

# Function to continuously play a tone in a separate thread
def play_tone(frequency, volume):
    global playback_thread, stop_thread
    print(f"Starting tone: frequency={frequency}, volume={volume}")
    stop_thread.clear()

    def play():
        while not stop_thread.is_set():
            try:
                print("Playing tone...")
                audio_data = generate_sine_wave(frequency, 0.1, volume)
                play_obj = sa.play_buffer(audio_data, 1, 2, 44100)
                play_obj.wait_done()
            except Exception as e:
                print(f"Error during playback: {e}")
                stop_thread.set()
                break
        print("Stopped playing tone.")

    playback_thread = threading.Thread(target=play)
    playback_thread.start()
    print("Tone playback thread started.")

# Function to stop playing the tone
def stop_tone():
    global stop_thread
    print("Stopping tone...")
    stop_thread.set()
    if playback_thread:
        playback_thread.join()
    print("Tone stopped.")

# Function to handle key press
def key_pressed(event, frequency, volume_slider):
    print(f"Key pressed: frequency={frequency}")
    volume = volume_slider.get() / 10
    play_tone(frequency, volume)

# Function to handle key release
def key_released(event):
    print("Key released.")
    stop_tone()

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
    btn.bind("<ButtonPress-1>", lambda event, freq=freq: key_pressed(event, freq, volume_slider))
    btn.bind("<ButtonRelease-1>", lambda event: key_released(event))

# Run the main event loop
print("Starting GUI...")
root.mainloop()
print("GUI loop ended.")
