import tkinter as tk
from tkinter import ttk
import numpy as np
import simpleaudio as sa
import threading
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

# Global variables for playback control
playback_thread = None
stop_thread = threading.Event()
play_event = threading.Event()
current_frequency = None
current_volume = 0.5

# Function to generate a sine wave
def generate_sine_wave(frequency, duration, volume):
    print(f"Generating sine wave: frequency={frequency}, duration={duration}, volume={volume}")
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave_data = 0.5 * volume * np.sin(2 * np.pi * frequency * t)
    audio_data = np.int16(wave_data * 32767)
    return audio_data

# Function to manage playback in a loop
def playback_manager():
    global current_frequency, current_volume

    while not stop_thread.is_set():
        print("Waiting for play event...")
        play_event.wait()  # Wait for a key press to start playback
        print("Play event triggered.")

        while play_event.is_set():  # Continue playing while key is pressed
            if current_frequency is not None:
                print(f"Playing tone: frequency={current_frequency}, volume={current_volume}")
                audio_data = generate_sine_wave(current_frequency, 0.1, current_volume)
                try:
                    play_obj = sa.play_buffer(audio_data, 1, 2, 44100)
                    play_obj.wait_done()
                    print("Tone playback completed.")
                except Exception as e:
                    print(f"Error during playback: {e}")
                    stop_thread.set()
                    break
            time.sleep(0.01)  # Small delay to manage CPU load and timing

    print("Playback thread terminating...")

# Function to start playing a tone
def start_playback(frequency, volume):
    global current_frequency, current_volume
    current_frequency = frequency
    current_volume = volume
    play_event.set()
    print(f"Started playback: frequency={frequency}, volume={volume}")

# Function to stop playing the tone
def stop_playback():
    play_event.clear()
    print("Stopped playback.")

# Function to handle key press
def key_pressed(event, frequency, volume_slider):
    print(f"Key pressed: frequency={frequency}")
    volume = volume_slider.get() / 10
    start_playback(frequency, volume)

# Function to handle key release
def key_released(event):
    print("Key released.")
    stop_playback()

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

# Start the playback thread
playback_thread = threading.Thread(target=playback_manager)
playback_thread.start()
print("Playback thread started.")

# Run the main event loop
print("Starting GUI...")
root.mainloop()

# Signal the playback thread to stop and wait for it to finish
stop_thread.set()
play_event.set()  # Trigger the thread to exit the loop
playback_thread.join()
print("GUI loop ended. Program terminated.")
