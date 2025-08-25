# Python Keylogger & Detector

This repository contains two Python scripts developed for educational purposes to demonstrate how a keylogger might function and how such a process could be detected.

## Screenshot
<img width="381" height="233" alt="image" src="https://github.com/user-attachments/assets/14c212cd-777f-40c3-9864-752dcdfd592b" />


## Features

-   `keylogger.py`: A simple keylogger that captures keyboard inputs and saves them to a log file.
    -   Logs standard alphanumeric characters.
    -   Handles special keys like Space, Enter, and Backspace.
    -   Saves all captured keystrokes to `key_log.txt`.
    -   Stops execution when the ESC key is pressed.

-   `detector.py`: A basic process scanner that looks for potential keylogger activity.
    -   Iterates through all running processes on the system.
    -   Scans process names for a list of suspicious keywords (e.g., "key", "log", "pynput").
    -   Reports any processes that match the keywords, along with their Process ID (PID).




## Disclaimer

This project is intended for educational and ethical purposes only. The code is provided to help users understand the potential security risks associated with keyloggers. Misusing this software for any malicious or unauthorized activities is strictly prohibited. The author assumes no responsibility for any damage or misuse of this code.




## Requirements

To run these scripts, you need Python 3 and a few external libraries.

-   Python 3.x
-   Libraries: `pynput`, `psutil`

You can install the required libraries using pip:

```bash
pip install pynput psutil
```




## How to Use

### 1. Running the Keylogger

To start capturing keystrokes, navigate to the project directory in your terminal and run:

```bash
python keylogger.py
```

The script will print a confirmation message and begin logging keystrokes to the `key_log.txt` file in the same directory. Press the ESC key to stop the keylogger.

### 2. Running the Detector

To scan for suspicious processes that might be keyloggers, run the detector script:

```bash
python detector.py
```

The script will scan all active processes and print a warning for any process whose name matches the keywords defined in the script.

