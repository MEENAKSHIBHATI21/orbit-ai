# Orbit AI 🛰️

Orbit AI is a Python-based satellite orbit visualization project that uses **TLE (Two-Line Element)** data from **CelesTrak** and the **SGP4 propagation model** to calculate and visualize satellite positions around Earth.

---

## Features

- Read and parse TLE files
- Compute satellite positions using SGP4
- Render a 3D Earth with Plotly
- Plot the International Space Station (ISS) in 3D space

---

## Tech Stack

- Python
- NumPy
- Plotly
- SGP4
- CelesTrak

---

## Project Structure

```text
orbit_ai/
├── data/
│   └── tle/
│       └── stations.tle
├── src/
│   ├── read_tle.py
│   ├── propagate.py
│   ├── visualizer.py
│   └── earth_iss.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Current Progress

- ✅ Read TLE files
- ✅ Parse orbital elements
- ✅ Propagate satellite positions
- ✅ Visualize Earth
- ✅ Plot the ISS

---

## Roadmap

- [x] Parse TLE data
- [x] SGP4 orbit propagation
- [x] 3D Earth visualization
- [x] Plot one satellite
- [ ] Draw complete orbit
- [ ] Animate satellite motion
- [ ] Multiple satellite visualization
- [ ] Ground tracks
- [ ] Live TLE updates
- [ ] Interactive dashboard

---

## Data Source

Satellite orbital data is obtained from **CelesTrak**.

---

## License

MIT 