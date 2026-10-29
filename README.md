# hue-utils

[![CI](https://github.com/zkm/hue-utils/actions/workflows/python-ci.yml/badge.svg)](https://github.com/zkm/hue-utils/actions/workflows/python-ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![phue](https://img.shields.io/badge/phue-5A5A5A)
![Philips Hue local bridge](https://img.shields.io/badge/Philips%20Hue-local%20bridge-0065D3?logo=philipshue&logoColor=white)

A simple Python utility to list and rename Philips Hue bulbs via the Hue Bridge API.  
Works entirely locally and doesn’t require any Philips Hue cloud login or mobile app.

## Features

- Connects to your Hue Bridge on your local network
- Lists all paired Hue bulbs
- Optionally rename bulbs
- Uses a `.env` file for secure local configuration

## Requirements

- Python 3.10+
- A Hue Bridge on your local network
- Philips Hue bulbs already paired with the bridge

## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/zkm/hue-utils.git
   cd hue-utils
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Hue Bridge's IP address:

   ```env
   HUE_BRIDGE_IP=192.168.x.x
   ```

   > 🔒 **Do not share this file or commit it to Git!**

## Usage

Run the script to list bulbs:

```bash
python hue_control.py
```

Sample output:

```
Your Hue bulbs:
ID 1: Living Room Lamp
ID 2: Kitchen Bar
ID 3: Desk Light
...
```

### Rename a bulb

To rename a bulb, edit the script and uncomment the section at the bottom:

```python
target_id = 2
new_name = "Studio Light"
lights[target_id].name = new_name
print(f"Renamed bulb {target_id} to '{new_name}'")
```

Then re-run the script.

---

## Snapshot / Markdown output

Running the main script will create a Markdown snapshot named `bulb_list.md` in the current working directory. The snapshot includes a table of lights (ID, name and current state) and a table of groups/rooms. This is useful for a quick inventory or for checking states without using the Hue app.

Notes:
- On first run the script may prompt you to press the Hue Bridge link button to authorize the app. Press it and re-run if you see a connection error.
- The repository includes `.env.example` with a placeholder for `HUE_BRIDGE_IP`. Copy it to `.env` and set your bridge IP before running.
- `bulb_list.md` and `.env` are listed in `.gitignore` by default so snapshots and local secrets won't be accidentally committed.

### License
This project is licensed under the [MIT LICENSE](LICENSE).
