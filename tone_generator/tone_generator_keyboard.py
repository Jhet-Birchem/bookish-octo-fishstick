import tkinter as tk
from tkinter import ttk
import numpy as np
import simpleaudio as sa
import asyncio

# Define piano keys (Octave C4 to C5)
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
current_frequency = None
current_volume = 0.5
play_event = asyncio.Event()
stop_event = asyncio.Event()

# Function to generate a sine wave
def generate_sine_wave(frequency, duration, volume):
    print(f"Generating sine wave: frequency={frequency}, duration={duration}, volume={volume}")
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave_data = 0.5 * volume * np.sin(2 * np.pi * frequency * t)
    audio_data = np.int16(wave_data * 32767)
    return audio_data

# Async function to manage playback
async def playback_manager():
    global current_frequency, current_volume

    while not stop_event.is_set():
        print("Waiting for play event...")
        await play_event.wait()
        print("Play event triggered.")

        while play_event.is_set() and not stop_event.is_set():
            if current_frequency is not None:
                print(f"Playing tone: frequency={current_frequency}, volume={current_volume}")
                audio_data = generate_sine_wave(current_frequency, 0.2, current_volume)
                play_obj = sa.play_buffer(audio_data, 1, 2, 44100)
                play_obj.wait_done()  # Wait for the audio playback to complete

            await asyncio.sleep(0.01)  # Small delay for the event loop to process other tasks

        print("Playback stopped.")

    print("Playback manager exiting...")

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

# Function to safely exit the program
def on_closing():
    stop_event.set()  # Signal the playback manager to exit
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Simple Piano")
root.protocol("WM_DELETE_WINDOW", on_closing)

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

# Start the playback manager as an asyncio task
async def main():
    asyncio.create_task(playback_manager())
    print("Playback manager started.")
    root.mainloop()

# Run the main event loop
asyncio.run(main())
