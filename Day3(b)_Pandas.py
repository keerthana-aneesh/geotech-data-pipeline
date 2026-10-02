import pandas as pd

data={
    "Borehole":[
        "BH01","BH01", "BH01", "BH01", "BH01", "BH01",
        "BH02", "BH02", "BH02", "BH02", "BH02",
        "BH03", "BH03", "BH03", "BH03", "BH03", "BH03", "BH03"
    ],
    "Depth_m":[1.5, 3.0, 4.5, 6.0, 9.0, 12.0,
        1.5, 4.5, 7.5, 10.5, 13.5,
        2.0, 3.5, 5.0, 7.0, 9.5, 11.0, 14.0

    ],
    "Soil_Type":[ "Sand", "Sand", "Silty Sand", "Silty Sand", "Clay", "Clay",
        "Sand", "Silty Sand", "Clay", "Clay", "Sand",
        "Sand", "Sand", "Silty Sand", "Silty Sand", "Clay", "Clay", "Sand"

    ],
    "SPT_N":[8, 12, 10, 14, 6, 15,
        6, 12, 5, 18, 28,
        9, 14, 11, 17, 7, 20, 35

    ],
     "Water_Content": [
        12, 14, 18, 20, 28, 26,
        10, 16, 30, 24, 11,
        13, 15, 19, 22, 32, 27, 9
    ],
    "Unit_Weight": [
        17.5, 18.0, 17.8, 18.2, 17.0, 18.0,
        17.0, 18.0, 16.8, 18.2, 19.2,
        17.6, 18.1, 17.9, 18.3, 17.1, 18.4, 19.5
    ]
}
df=pd.DataFrame(data)
print(df)

print(df.groupby("Soil_Type")["SPT_N"].mean())
print(df.groupby("Soil_Type")["Water_Content"].agg(["min","max","mean"]))
print(df["Soil_Type"].value_counts())

# Creating New Columns
df["Depth_ft"]=df["Depth_m"]*3.281
df["Total_Stress"]=df["Depth_m"]*df["Unit_Weight"]

Water_Table=2.0
df["Pore_Pressure"]=(df["Depth_m"]-Water_Table)*9.81
df["Pore_Pressure"]=df["Pore_Pressure"].clip(lower=0)

df["Effective_Stress"]=df["Total_Stress"]-df["Pore_Pressure"]
print(df)

#Conditional Column
import numpy as np
df["Density"]=np.where(df["SPT_N"]>30,"Dense","Loose")
print(df)

def plasticity(wc):
    if wc < 35:
        return "Low"
    elif wc < 50:
        return"Medium"
    else:
        return "High"
df["Plasticity"]=df["Water_Content"].apply(plasticity)
print (df)

def soiltype(ST):
    if ST=="Clay":
        return "Yes"
    else:
        return "No"
df["Clay_Flag"]=df["Soil_Type"].apply(soiltype)
print(df)

df.to_csv("soil_data_processed.csv", index=False)
df.to_excel("soil_data_processed.xlsx", index=False, sheet_name="Processed")
with pd.ExcelWriter("geotech_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="All_Data", index=False)
    df.groupby("Soil_Type")["SPT_N"].mean().to_excel(writer, sheet_name="Summary")