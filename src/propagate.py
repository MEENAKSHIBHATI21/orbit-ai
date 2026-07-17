from sgp4.api import Satrec
from sgp4.api import jday
from datetime import datetime, timezone

# Read the TLE file
file_path = "../data/tle/stations.tle"

with open(file_path, "r") as file:
    lines = file.readlines()

# Get the first satellite (ISS)
name = lines[0].strip()
line1 = lines[1].strip()
line2 = lines[2].strip()

print("Satellite:", name)

# Create the satellite object
satellite = Satrec.twoline2rv(line1, line2)

# Get the current UTC time
now = datetime.now(timezone.utc)

# Convert the time to Julian Date
jd, fr = jday(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second + now.microsecond / 1e6
)

# Calculate the satellite position
error, position, velocity = satellite.sgp4(jd, fr)

if error == 0:
    print("\nPosition (km):")
    print(position)

    print("\nVelocity (km/s):")
    print(velocity)
else:
    print("Propagation error:", error)