def void_ratio_and_dry_unit_weight(
        total_vol:float,
        total_mass:float,
        water_content:float,
        specific_gravity:float,
        rho_w:float=1000,
        g:float=9.81
)->tuple[float,float]:
    """
    Compute void ratio and dry unit weight from basic soil properties.

    Parameters
    ----------
    total_vol : float
        Total volume of the soil sample (m^3).
    total_mass : float
        Total mass of the soil sample (kg).
    water_content : float
        Water content as a decimal (e.g., 0.15 for 15%).
    specific_gravity : float
        Specific gravity of solids (dimensionless).
    rho_w : float
        Density of water (kg/m^3). Default 1000.
    g : float
        Acceleration due to gravity (m/s^2). Default 9.81.

    Returns
    -------
    tuple[float, float]
        Void ratio (e) and dry unit weight (kN/m^3).
    """

    if total_vol<=0 or total_mass<=0:
        raise ValueError("Total volume and total mass must be positive.")
    if water_content<=0:
        raise ValueError("Water content cannot be negative.")
    if specific_gravity <= 0:
        raise ValueError("Specific gravity must be positive.")

    mass_solids = total_mass / (1 + water_content)
    vol_solids = mass_solids / (specific_gravity * rho_w)
    vol_voids = total_vol - vol_solids
    vol_voids = total_vol - vol_solids
    e = vol_voids / vol_solids
    gamma_d = (mass_solids * g) / total_vol / 1000  # kN/m^3
    return e, gamma_d

if __name__ == "__main__":
    e, gamma_d = void_ratio_and_dry_unit_weight(0.5, 900, 0.15, 2.65)
    print(f"Void ratio: {round(e, 3)}")
    print(f"Dry unit weight: {round(gamma_d, 2)} kN/m^3")