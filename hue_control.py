import os
from dotenv import load_dotenv
from phue import Bridge

# Load .env file
load_dotenv()

# Get bridge IP from env
BRIDGE_IP = os.getenv('HUE_BRIDGE_IP')

if not BRIDGE_IP:
    raise ValueError("HUE_BRIDGE_IP environment variable is not set.")

# Connect to bridge
b = Bridge(BRIDGE_IP)
b.connect()

# List bulbs
lights = b.get_light_objects('id')
print("Your Hue bulbs:")
for light_id, light in lights.items():
    print(f"ID {light_id}: {light.name}")
