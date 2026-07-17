file_path = "../data/tle/stations.tle"

with open(file_path, "r") as file:
    lines = file.readlines()

for i in range(0, len(lines), 3):
    name = lines[i].strip()
    line1 = lines[i + 1].strip()
    line2 = lines[i + 2].strip()

    print(f"Satellite: {name}")
    print(line1)
    print(line2)
    print("-" * 50)