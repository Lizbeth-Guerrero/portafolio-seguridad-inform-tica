import datetime
from pynput.keyboard import Key, Listener

LOG_FILE = "keylog.txt"
counter = 0

def get_key_str(key):
    try:
        return key.char if key.char is not None else str(key)
    except AttributeError:
        return str(key)

def log_event(event_type, key):
    global counter
    counter += 1
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    key_str = get_key_str(key)
    event_id = f"evento_{counter:03d}"
    
    log_entry = f"{timestamp} | {event_type} ({key_str}) | {event_id}\n"
    print(log_entry.strip())
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def on_press(key):
    log_event("PRESS", key)

def on_release(key):
    log_event("RELEASE", key)
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




