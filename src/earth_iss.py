import numpy as np
import plotly.graph_objects as go

from sgp4.api import Satrec, jday
from datetime import datetime, timezone

# ------------------------
# Read ISS TLE
# ------------------------

file_path = "../data/tle/stations.tle"

with open(file_path, "r") as file:
    lines = file.readlines()

name = lines[0].strip()
line1 = lines[1].strip()
line2 = lines[2].strip()

satellite = Satrec.twoline2rv(line1, line2)

# ------------------------
# Current time
# ------------------------

now = datetime.now(timezone.utc)

jd, fr = jday(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
)

error, position, velocity = satellite.sgp4(jd, fr)

x_sat, y_sat, z_sat = position

# ------------------------
# Draw Earth
# ------------------------

radius = 6371

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = radius * np.outer(np.cos(u), np.sin(v))
y = radius * np.outer(np.sin(u), np.sin(v))
z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

fig = go.Figure()

fig.add_surface(
    x=x,
    y=y,
    z=z,
    opacity=0.9,
    showscale=False
)

# ------------------------
# Draw ISS
# ------------------------

fig.add_trace(
    go.Scatter3d(
        x=[x_sat],
        y=[y_sat],
        z=[z_sat],
        mode="markers",
        marker=dict(size=5),
        name=name
    )
)

fig.update_layout(
    title="Earth + ISS",
    scene=dict(
        aspectmode="data"
    )
)

fig.show()