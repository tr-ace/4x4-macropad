# https://github.com/tr-ace/4x4-macropad

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

# Matrix Pins
keyboard.row_pins = (
    board.D0,  # Row 1
    board.D1,  # Row 2
    board.D2,  # Row 3
    board.D3,  # Row 4
)

keyboard.col_pins = (
    board.D4,  # Col 1
    board.D5,  # Col 2
    board.D6,  # Col 3
    board.D7,  # Col 4
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Map macro keys below (Col 1 / Row 1 is the key closest to the USB C port)
keymap = [
        # Col 1,                          Col 2,            Col 3,                         Col 4
        KC.LCTL(KC.Z),                    KC.LCTL(KC.Y),     KC.LGUI(KC.LSFT(KC.S)),       KC.LGUI(KC.TAB),   # Row 4

        KC.LGUI(KC.M),                    KC.LGUI(KC.E),     KC.LCTL(KC.F),                KC.LCTL(KC.H),     # Row 3

        KC.LCTL(KC.LSFT(KC.M)),           KC.MUTE,           KC.AUDIO_VOL_DOWN,            KC.AUDIO_VOL_UP,   # Row 2

        KC.LCTL(KC.A),                    KC.LCTL(KC.C),     KC.LCTL(KC.V),                KC.LCTL(KC.S),     # Row 1
]

formatted_keymap = []

# Reverse keymap so it logically lines up with the physical keys
for i in range(0, len(keymap), 4):
    current_group = keymap[i:i + 4]
    formatted_keymap.extend(list(reversed(current_group)))


keyboard.keymap = [formatted_keymap]


if __name__ == '__main__':
    keyboard.go()

