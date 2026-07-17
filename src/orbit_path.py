import numpy as np
import plotly.graph_objects as go

from sgp4.api import Satrec, jday
from datetime import datetime, timezone, timedelta

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
# Current UTC Time
# ------------------------

now = datetime.now(timezone.utc)

# Lists to store orbit points
x_points = []
y_points = []
z_points = []

# ------------------------
# Calculate orbit for next 90 minutes
# ------------------------

for second in range(0, 5600, 10):

    # Advance time by 'second' seconds
    current_time = now + timedelta(seconds=second)

    # Convert to Julian Date
    jd, fr = jday(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second + current_time.microsecond / 1e6
    )

    error, position, velocity = satellite.sgp4(jd, fr)

    if error == 0:
        x, y, z = position

        x_points.append(x)
        y_points.append(y)
        z_points.append(z)

# ------------------------
# Draw Earth
# ------------------------

radius = 6371

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

earth_x = radius * np.outer(np.cos(u), np.sin(v))
earth_y = radius * np.outer(np.sin(u), np.sin(v))
earth_z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

fig = go.Figure()

fig.add_surface(
    x=earth_x,
    y=earth_y,
    z=earth_z,
    opacity=0.9,
    showscale=False
)

# ------------------------
# Draw Orbit Path
# ------------------------

fig.add_trace(
    go.Scatter3d(
        x=x_points,
        y=y_points,
        z=z_points,
        mode="lines",
        line=dict(width=4),
        name="Orbit"
    )
)

# ------------------------
# Draw ISS (current position)
# ------------------------

fig.add_trace(
    go.Scatter3d(
        x=[x_points[0]],
        y=[y_points[0]],
        z=[z_points[0]],
        mode="markers",
        marker=dict(size=6),
        name=name
    )
)

fig.update_layout(
    title="ISS Orbit Around Earth",
    scene=dict(
        aspectmode="data"
    )
)

fig.show()