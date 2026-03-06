### **Project Tri-Dragon : Constellation Conjunction Analysis**





This is a Space Situational Awareness (SSA) project designed to track and analyze the relative motion of three satellites — **Drogon, Rhaegal,** and **Viserion** in a multi-inclination constellation. 



##### **Mission:**



The goal of this project was to simulate a high-fidelity orbital environment to see if these three satellites ever risk a close approach (conjunction). Then built the mission in GMAT (General Mission Analysis Tool) using a JGM2 Gravity Model to account for Earth's non-spherical shape. Later, took that raw orbital data and built a Python-based analysis tool to monitor the safety distance between the assets.



##### **How it Works:**



* **The Setup       :** The constellation is spread across three different orbital planes (30 degree, 45 degree, and 60 degree inclinations).
* The Data        : GMAT outputs the state vectors (X, Y, Z, VX, VY, VZ) in the Earth-Centered Inertial (ECI) frame.
* The Analysis    : Using NumPy and Pandas, python script calculates the 3D Euclidean distance between every pair of satellites at every single second of the 24-hour mission.
* The Alert System: If any two satellites drop below a 10 km screening volume, the script flags it as a potential conjunction.



##### **Repository Structure:**



* /data       : Contains the CSV files for the three "Dragons".
* /python\_file: The main Python engine (TriDrag.py) for analysis and plotting.
* /gmat\_model : The original .script file used to generate the data.
* /output     : Plots of Orbital View, Ground Track, Satellite Orbit Visualization (ECI frame) and Inter-Satellite Distance Analysis.



##### **Current Findings:**



After running the analysis on a 24-hour (86400s) propagation:

Status: Safe.

Closest Distance: ~7,261 km (between Drogon and Viserion).

Observation: Because of the staggered RAAN and differing inclinations, these satellites maintain a very healthy distance, even though their orbits cross.



#Clement\_Davis

