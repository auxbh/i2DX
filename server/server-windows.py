import sys
import libi2dx
from os import path
import keyboard
from configparser import ConfigParser

def toggle(key_char, state):
    print(f"Key Character: {key_char}, State: {state}")
    if state:
        keyboard.press(key_char)
    else:
        keyboard.release(key_char)

class I2DXWebSocketAutoPy(libi2dx.I2DXWebSocket):
    def toggle_key(self, key_id, state, player):
        try:
            key_char = libi2dx.config.get('keymap_player%s' % player, key_id)
            print(f"Toggling key: {key_char}, State: {state}")
            toggle(key_char, state)
        except ConfigParser.NoOptionError:
            print("Key map not found for %s, player %s" % (key_id, player))

if __name__ == "__main__":
    libi2dx.serve(I2DXWebSocketAutoPy)
