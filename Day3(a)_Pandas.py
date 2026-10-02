import pandas as pd
data ={
    "depth_m":[1.5,3,4.5,6],
    "Soil_type":["Sand","Silt","Clay","Clay"],
    "SPT_N":[8,12,6,18]
}
df=pd.DataFrame(data)
print(df)

# Importing Pandas
import pandas as pd
data1={
    "Depth_m":[2,4,6],
    "Soil_Type":["sand","Silt","Clay"],
    "Water_Content":[10,18,30]
}
df1=pd.DataFrame(data1)
print(df1)

#Inspecting DataFrame
print(df1.head(2))
print(df1.shape)
print(list(df1.columns))
print(df1.info())
print(df1.describe())
#Selecting Columns
print(df1["Soil_Type"])
print(df1[["Soil_Type","Water_Content"]])

#Filtering Rows
print(df1[df1["Depth_m"] > 3])
print(df1[df1["Soil_Type"] =="sand"])
print(df1[(df1["Water_Content"] > 15) & (df1["Soil_Type"] == "sand")])
print(df1[df1["Soil_Type"].isin(["sand","Clay"])])

#Sorting
print(df1.sort_values("Water_Content"))
print(df1.sort_values("Water_Content",ascending=False))
print(df1.sort_values(["Soil_Type","Depth_m"]))

#Groupby
print(df1.groupby("Soil_Type")["Depth_m"].mean())
print(df1.groupby("Soil_Type")["Water_Content"].agg(["mean","median","min","max"]))