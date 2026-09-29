# Integer
num_layers=5
# Float
water_table_depth=3.2
# String
project_name="Saadiyat Lagoons"
# Boolean
is_saturated = True

print(project_name,"has",num_layers,"soil layers.")

# lists
soil_types=["Sand","Clay","Silt","Gravel"]
print(soil_types)
print(soil_types[0])
soil_types.append("Peat")
print(soil_types)
soil_types[1]="Rock"
soil_types.insert(2,"Peat")
print(soil_types)
count = soil_types.count("Peat")
print(count)

# Dictionaries
Soil_params ={
    "unit_weight": 18.5,
    "Friction_angle":32,
    "cohesion": 0
}
print(Soil_params)
print(Soil_params["Friction_angle"])

# Loops
for layer in soil_types:
 print("layer:",layer)

# Funstions

def dry_unit_weight(Gs,e,gamma_w=9.81):
 return (Gs*gamma_w)/(1+e)

# ask user for inputs
Gs=float(input("Enter Gs :"))
e = float(input("Enter e :"))

result =dry_unit_weight(Gs,e)
print("Dry unit weight:",round(result,2),"kN/m3")
result1 =dry_unit_weight(2.56,.85)
print("Dry unit weight:",round(result1,2),"kN/m3")


# Diagnostic Question

def void_ratio(total_vol,total_mass,water_content,specific_gravity,rho_w = 1000):

 M_S = (total_mass)/(1+water_content)
 V_S = (M_S)/(specific_gravity*rho_w)
 V_V= total_vol-V_S

 e = V_V/V_S
 return e

total_vol = float(input("Enter Total Volume:"))
total_mass = float(input("Enter Total Mass:"))
water_content = float(input("Enter Water Content:"))
specific_gravity = float(input("Enter Specific Gravity:"))

e=void_ratio(total_vol, total_mass, water_content, specific_gravity)
print("Void ratio:", round(e, 3))