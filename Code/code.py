import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

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


CALC = simple_key_sequence([
    KC.LGUI(KC.R),
    KC.DELAY(100),
    KC.C, KC.A, KC.L, KC.C,
    KC.ENTER
])

TERMINAL = simple_key_sequence([
    KC.LGUI(KC.X),
    KC.DELAY(100),
    KC.I
])


# Map macro keys below (Col 1 / Row 1 is the key closest to the USB C port)
keyboard.keymap = [
    [
        # Col 1,                          Col 2,            Col 3,                        Col 4

        KC.LCTL(KC.A),                    KC.LCTL(KC.C),     KC.LCTL(KC.V),                KC.LCTL(KC.S),   # Row 1

        KC.LCTL(KC.LSFT(KC.M)),           KC.MUTE,           KC.VOLD,                      KC.VOLU,         # Row 2

        KC.LGUI(KC.M),                    KC.LGUI(KC.E),     TERMINAL,                     CALC,            # Row 3

        KC.LCTL(KC.Z),                    KC.LCTL(KC.Y),     KC.LGUI(KC.LSFT(KC.S)),       KC.LGUI(KC.TAB), # Row 4
    ]
]

if __name__ == '__main__':
    keyboard.go()
