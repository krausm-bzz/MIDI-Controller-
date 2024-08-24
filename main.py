import tkinter as tk
from mido import Message, open_output

class MidiController:
    def __init__(self, master):
        self.master = master
        self.master.title("Einfacher MIDI-Controller")

        self.midi_port = None
        self.connect_midi()

        # Create a label and entry for the note number
        self.label_note = tk.Label(master, text="Note Number (0-127):")
        self.label_note.pack()

        self.note_entry = tk.Entry(master)
        self.note_entry.pack()
        self.note_entry.insert(0, "60")  # Default to Middle C (C4)

        # Create buttons
        self.button_on = tk.Button(master, text="Note On", command=self.note_on)
        self.button_on.pack(pady=10)

        self.button_off = tk.Button(master, text="Note Off", command=self.note_off)
        self.button_off.pack(pady=10)

    def connect_midi(self):
        try:
            # Connect to the first available MIDI output port
            self.midi_port = open_output(mido.get_output_names()[0])
        except Exception as e:
            print(f"Error connecting to MIDI output: {e}")
            self.midi_port = None

    def note_on(self):
        if self.midi_port:
            note = int(self.note_entry.get())  # Get the note number from the entry
            msg = Message('note_on', note=note, velocity=64)
            self.midi_port.send(msg)
            print(f"Note On sent for note {note}")

    def note_off(self):
        if self.midi_port:
            note = int(self.note_entry.get())  # Get the note number from the entry
            msg = Message('note_off', note=note, velocity=64)
            self.midi_port.send(msg)
            print(f"Note Off sent for note {note}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MidiController(root)
    root.mainloop()
