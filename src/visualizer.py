import numpy as np
import plotly.graph_objects as go

radius = 6371  # Earth's radius in km

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

fig.show()