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

# Get bulbs
lights = b.get_light_objects('id')
print("Your Hue bulbs:")
for light_id, light in lights.items():
    print(f"ID {light_id}: {light.name}")

# Output to Markdown file
with open("bulb_list.md", "w") as f:
    f.write("# Hue Bulbs\n\n")
    f.write("| ID | Name |\n")
    f.write("|----|------|\n")
    for light_id, light in lights.items():
        f.write(f"| {light_id} | {light.name} |\n")

