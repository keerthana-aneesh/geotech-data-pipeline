import os
from plxscripting.easy import *

# ---------------------------------------------------------------
# Settings
# ---------------------------------------------------------------
HOST = "localhost"
PORT = 10000                      # Must match PLAXIS: Expert > Configure remote scripting server
PASSWORD = "WcRH%vfGzVW@$<3X"         # Replace with the password shown in PLAXIS

MODEL_WIDTH = 20.0                # m
MODEL_DEPTH = 10.0                # m
SAVE_PATH = r"C:\GEOTECHNICAL ENGINEERING\Python\Python basics\geotech-data-pipeline\data\automated_model.p2dx"

# ---------------------------------------------------------------
# Connect to PLAXIS Input
# ---------------------------------------------------------------
s_i, g_i = new_server(HOST, PORT, password=PASSWORD)

# Start a new project
s_i.new()

# ---------------------------------------------------------------
# Geometry: ground level at y = 0, model extends 10 m downward
# ---------------------------------------------------------------
g_i.SoilContour.initializerectangular(0, -MODEL_DEPTH, MODEL_WIDTH, 0)

# Borehole and a single soil layer filling the full depth
g_i.borehole(0)
g_i.soillayer(MODEL_DEPTH)

# ---------------------------------------------------------------
# Material: Mohr-Coulomb sand (individual assignment, not setproperties)
# ---------------------------------------------------------------
sand = g_i.soilmat()
sand.Identification = "Sand"
sand.SoilModel = 2                # 1 = Linear Elastic, 2 = Mohr-Coulomb
sand.DrainageType = 0             # 0 = Drained
sand.gammaUnsat = 17              # kN/m3
sand.gammaSat = 20                # kN/m3
sand.Gref = 11538                 # kN/m2  (E = 2G(1+nu) ~ 30,000 kPa)
sand.nu = 0.3
sand.cref = 0.1                   # kN/m2, small value avoids numerical issues
sand.phi = 32                     # degrees
sand.psi = 2                      # degrees, dilation angle (phi - 30)

# Assign material to the soil layer
g_i.Soils[0].Material = sand

# ---------------------------------------------------------------
# Save
# ---------------------------------------------------------------
# The folder must exist on the machine running PLAXIS
os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
g_i.save(SAVE_PATH)

print("Model created and saved successfully.")