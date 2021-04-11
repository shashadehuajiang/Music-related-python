# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

import midi
#pattern = midi.read_midifile("Rec0001.wav.mid")
#print (pattern)



from midi2audio import FluidSynth
#FluidSynth().play_midi("./Rec0001.wav.mid")

# using the default sound font in 44100 Hz sample rate
#fs = FluidSynth()
#fs.midi_to_audio('Rec0001.wav.mid', 'output.wav')


import pygame

def play_midi(file):
   freq = 44100
   bitsize = -16
   channels = 2
   buffer = 1024
   pygame.mixer.init(freq, bitsize, channels, buffer)
   pygame.mixer.music.set_volume(1)
   clock = pygame.time.Clock()
   try:
       pygame.mixer.music.load(file)
   except:
       import traceback
       print(traceback.format_exc())
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
       clock.tick(30)


play_midi('Rec0001.wav.mid')






