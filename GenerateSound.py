from pydub.generators import Sine
from pydub.playback import play

import math

class GenerateSound:
    def __init__(self, notes):
        self.notes = notes
        self.pitch_map = {'C': 261.63, 'D': 293.66, 'E': 329.63, 'F': 349.23, 
                          'G': 392.00, 'A': 440.00, 'B': 493.88}  
        self.duration_map = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 's': 0.25}
        self.sample_rate = 44100

    def get_frequency(self, pitch, octave):
        base_freq = self.pitch_map[pitch]
        return base_freq * (2 ** (octave - 4))  

    def generate_single_sound(self, frequency, duration):
        return Sine(frequency).to_audio_segment(duration=duration * 1000)

    def generateSound(self):
        sounds = []

        for note in self.notes:
            pitch = note[0] 
            octave = int(note[1])  
            duration = note[2]  

            frequency = self.get_frequency(pitch, octave)
            duration_in_seconds = self.duration_map[duration]

            sound = self.generate_single_sound(frequency, duration_in_seconds)
            sounds.append(sound)

        combined_sound = sum(sounds)  
        combined_sound.export("output.wav", format="wav")  
        play(combined_sound)  
