# hue-utils

A simple Python utility to list and rename Philips Hue bulbs via the Hue Bridge API.  
Works entirely locally and doesn’t require any Philips Hue cloud login or mobile app.

## Features

- Connects to your Hue Bridge on your local network
- Lists all paired Hue bulbs
- Optionally rename bulbs
- Uses a `.env` file for secure local configuration

## Requirements

- Python 3.7+
- A Hue Bridge on your local network
- Philips Hue bulbs already paired with the bridge

## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/hue-utils.git
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

### License
This project is licensed under the [MIT LICENSE](LICENSE).