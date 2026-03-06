import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. SETUP PATHS (Makes the project portable for GitHub)
# Gets the folder where this script (TriDrag.py) is saved
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
output_dir = os.path.join(base_dir, "output")

# Create output folder automatically if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 2. LOAD CSV FILES
# This looks into your 'data' folder for the files
try:
    drogon = pd.read_csv(os.path.join(data_dir, "Drogon.csv"))
    rhaegal = pd.read_csv(os.path.join(data_dir, "Rhaegal.csv"))
    viserion = pd.read_csv(os.path.join(data_dir, "Viserion.csv"))
    print("Data successfully loaded from /data folder.")
except FileNotFoundError:
    print(f"Error: Could not find CSVs in {data_dir}. Ensure your files are named correctly.")
    exit()

# Align lengths to ensure data consistency
min_len = min(len(drogon), len(rhaegal), len(viserion))
drogon = drogon.iloc[:min_len]
rhaegal = rhaegal.iloc[:min_len]
viserion = viserion.iloc[:min_len]

# 3. EXTRACT POSITION DATA
dx, dy, dz = drogon["Drogon.EarthMJ2000Eq.X"], drogon["Drogon.EarthMJ2000Eq.Y"], drogon["Drogon.EarthMJ2000Eq.Z"]
rx, ry, rz = rhaegal["Rhaegal.EarthMJ2000Eq.X"], rhaegal["Rhaegal.EarthMJ2000Eq.Y"], rhaegal["Rhaegal.EarthMJ2000Eq.Z"]
vx, vy, vz = viserion["Viserion.EarthMJ2000Eq.X"], viserion["Viserion.EarthMJ2000Eq.Y"], viserion["Viserion.EarthMJ2000Eq.Z"]

# Convert to arrays
d_pos = np.column_stack((dx, dy, dz))
r_pos = np.column_stack((rx, ry, rz))
v_pos = np.column_stack((vx, vy, vz))

# 4. 3D ORBIT VISUALIZATION
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(dx, dy, dz, label="Drogon", color='red')
ax.plot(rx, ry, rz, label="Rhaegal", color='gold')
ax.plot(vx, vy, vz, label="Viserion", color='cyan')

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title("Satellite Orbit Visualization (ECI Frame)")
ax.legend()

# Save plot to output folder
plt.savefig(os.path.join(output_dir, "orbit_visualization.png"), dpi=300)

# 5. DISTANCE CALCULATION & CONJUNCTION DETECTION
dist_dr = np.linalg.norm(d_pos - r_pos, axis=1)
dist_dv = np.linalg.norm(d_pos - v_pos, axis=1)
dist_rv = np.linalg.norm(r_pos - v_pos, axis=1)

threshold = 10  # km
print("\nPotential Conjunction Alerts:\n")
found_conjunction = False
for i in range(len(dist_dr)):
    if dist_dr[i] < threshold:
        print(f"Drogon - Rhaegal approach at step {i}: {dist_dr[i]:.2f} km")
        found_conjunction = True
    if dist_dv[i] < threshold:
        print(f"Drogon - Viserion approach at step {i}: {dist_dv[i]:.2f} km")
        found_conjunction = True
    if dist_rv[i] < threshold:
        print(f"Rhaegal - Viserion approach at step {i}: {dist_rv[i]:.2f} km")
        found_conjunction = True

if not found_conjunction:
    print("No conjunctions detected within the 10km threshold.")

# 6. DISTANCE vs TIME PLOT
plt.figure(figsize=(10, 6))
plt.plot(dist_dr, label="Drogon - Rhaegal")
plt.plot(dist_dv, label="Drogon - Viserion")
plt.plot(dist_rv, label="Rhaegal - Viserion")
plt.axhline(threshold, color='red', linestyle="--", label="Collision Threshold")
plt.xlabel("Time Step")
plt.ylabel("Distance (km)")
plt.title("Inter-Satellite Distance Analysis")
plt.legend()
plt.grid(True)

# Save plot to output folder
plt.savefig(os.path.join(output_dir, "distance_analysis.png"), dpi=300)

print(f"\nAnalysis complete. Plots saved to: {output_dir}")