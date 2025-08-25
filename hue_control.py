#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
from phue import Bridge

load_dotenv()  # loads .env in CWD by default; pass dotenv_path=... if needed
BRIDGE_IP = os.getenv("HUE_BRIDGE_IP")
if not BRIDGE_IP:
    print("Error: HUE_BRIDGE_IP is not set in your .env", file=sys.stderr)
    sys.exit(2)

b = Bridge(BRIDGE_IP)

try:
    # On first run you may need to press the bridge link button
    b.connect()
except Exception as e:
    print(f"Failed to connect to Hue Bridge at {BRIDGE_IP}.\n{e}\n"
          "Tip: press the link button and re-run.", file=sys.stderr)
    sys.exit(1)

# Lights
lights_by_id = b.get_light_objects('id')
sorted_items = sorted(lights_by_id.items(), key=lambda kv: int(kv[0]))

print("Your Hue bulbs:")
for lid, light in sorted_items:
    print(f"ID {lid}: {light.name}")

# Groups / Rooms
groups = b.get_group()  # dict keyed by group id
print("\nGroups/Rooms:")
for gid, g in groups.items():
    print(f"ID {gid}: {g.get('name')}  (lights: {', '.join(g.get('lights', []))})")

# Write Markdown snapshot
with open("bulb_list.md", "w", encoding="utf-8") as f:
    f.write("# Hue Snapshot\n\n")
    f.write("## Lights\n\n")
    f.write("| ID | Name | On | Bri | CT | XY |\n")
    f.write("|---:|------|:--:|----:|---:|-----|\n")
    for lid, light in sorted_items:
        state = {}
        try:
            state = b.get_light(int(lid))["state"]
        except Exception:
            pass
        on = "✅" if state.get("on") else "❌"
        bri = state.get("bri", "")
        ct  = state.get("ct", "")
        xy  = state.get("xy", "")
        f.write(f"| {lid} | {light.name} | {on} | {bri} | {ct} | {xy} |\n")

    f.write("\n## Groups / Rooms\n\n")
    f.write("| ID | Name | Light IDs |\n")
    f.write("|---:|------|-----------|\n")
    for gid, g in groups.items():
        f.write(f"| {gid} | {g.get('name')} | {', '.join(g.get('lights', []))} |\n")

