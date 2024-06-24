import pandas as pd

def calculate_costs(direct_material_cost, direct_labor_cost, other_direct_cost, production_units, operating_overhead, company_overhead, operating_base="material", company_base="restricted"):
    # Közvetlen költségek összesítése
    total_direct_cost = [a + b + c for a, b, c in zip(direct_material_cost, direct_labor_cost, other_direct_cost)]

    # Üzemi általános költség elosztása
    if operating_base == "material" or operating_base == "anyagköltség":
        base_operating = direct_material_cost
    elif operating_base == "labor" or operating_base == "bérköltség":
        base_operating = direct_labor_cost
    elif operating_base == "other" or operating_base == "egyéb költség":
        base_operating = other_direct_cost
    elif operating_base == "direct" or operating_base == "összes közvetlen költség":
        base_operating = total_direct_cost
    else:
        raise ValueError("Invalid operating base. Choose 'material', 'labor', 'other' or 'direct' (anyagköltség, bérköltség, egyéb költség vagy összes közvetlen költség).")

    total_base_operating = sum(base_operating)
    operating_overhead_allocation = [bo / total_base_operating * operating_overhead for bo in base_operating]

    # Szűkített költségek összesítése
    restricted_costs = [tdc + oha for tdc, oha in zip(total_direct_cost, operating_overhead_allocation)]

    # Vállalati általános költség elosztása
    if company_base == "restricted" or company_base == "szűkített költség":
        base_company = restricted_costs
    elif company_base == "direct" or company_base == "összes közvetlen költség":
        base_company = total_direct_cost
    else:
        raise ValueError("Invalid company base. Choose 'restricted' or 'direct' (szűkített költség vagy összes közvetlen költség).")

    total_base_company = sum(base_company)
    company_overhead_allocation = [bc / total_base_company * company_overhead for bc in base_company]

    # Teljes költségek összesítése
    total_costs = [rc + coa for rc, coa in zip(restricted_costs, company_overhead_allocation)]

    # Önköltség darabonként
    unit_costs = [tc / pu for tc, pu in zip(total_costs, production_units)]

    # Közvetlen önköltség darabonként
    direct_unit_costs = [tdc / pu for tdc, pu in zip(total_direct_cost, production_units)]

    # Szűkített önköltség darabonként
    restricted_unit_costs = [rc / pu for rc, pu in zip(restricted_costs, production_units)]

    return {
        "total_direct_cost": total_direct_cost,
        "operating_overhead_allocation": operating_overhead_allocation,
        "restricted_costs": restricted_costs,
        "company_overhead_allocation": company_overhead_allocation,
        "total_costs": total_costs,
        "unit_costs": unit_costs,
        "direct_unit_costs": direct_unit_costs,
        "restricted_unit_costs": restricted_unit_costs
    }

# Kérdések nyelv szerint
print("Enter the allocation base for operating overhead ('material', 'labor', 'other' or 'direct') / Adja meg az üzemi általános költségek vetítési alapját ('anyagköltség', 'bérköltség', 'egyéb költség' vagy 'összes közvetlen költség'):")
operating_base = input().strip().lower()
print("Enter the allocation base for company overhead ('restricted' or 'direct') / Adja meg a vállalati általános költségek vetítési alapját ('szűkített költség' vagy 'összes közvetlen költség'):")
company_base = input().strip().lower()

# Ellenőrzés
valid_operating_bases = ["material", "labor", "other", "direct", "anyagköltség", "bérköltség", "egyéb költség", "összes közvetlen költség"]
valid_company_bases = ["restricted", "direct", "szűkített költség", "összes közvetlen költség"]

if operating_base not in valid_operating_bases:
    raise ValueError("Invalid operating base. Please choose 'material', 'labor', 'other' or 'direct' / Érvénytelen üzemi vetítési alap. Kérem adjon meg 'anyagköltség', 'bérköltség', 'egyéb költség' vagy 'összes közvetlen költség'.")
if company_base not in valid_company_bases:
    raise ValueError("Invalid company base. Please choose 'restricted' or 'direct' / Érvénytelen vállalati vetítési alap. Kérem adjon meg 'szűkített költség' vagy 'összes közvetlen költség'.")

# Adatok
direct_material_cost = [600, 400]  # Közvetlen anyagköltség
direct_labor_cost = [300, 250]  # Közvetlen bérköltség
other_direct_cost = [420, 230]  # Egyéb közvetlen költség
production_units = [10, 25]  # Előállított termékek száma
operating_overhead = 500  # Üzemi általános költség
company_overhead = 810  # Vállalati általános költség

# Számítások
results = calculate_costs(direct_material_cost, direct_labor_cost, other_direct_cost, production_units, operating_overhead, company_overhead, operating_base, company_base)

# Eredmények megjelenítése
data = {
    "Megnevezés": ["Közvetlen anyagköltség", "Közvetlen bérköltség", "Egyéb közvetlen költség", "Összes közvetlen költség", "Üzemi általános költség", "Szűkített költség", "Vállalati általános költség", "ÖSSZES KÖLTSÉG"],
    "A termék (eFt)": [direct_material_cost[0], direct_labor_cost[0], other_direct_cost[0], results["total_direct_cost"][0], results["operating_overhead_allocation"][0], results["restricted_costs"][0], results["company_overhead_allocation"][0], results["total_costs"][0]],
    "B termék (eFt)": [direct_material_cost[1], direct_labor_cost[1], other_direct_cost[1], results["total_direct_cost"][1], results["operating_overhead_allocation"][1], results["restricted_costs"][1], results["company_overhead_allocation"][1], results["total_costs"][1]],
    "Vállalati összesen (eFt)": [sum(direct_material_cost), sum(direct_labor_cost), sum(other_direct_cost), sum(results["total_direct_cost"]), sum(results["operating_overhead_allocation"]), sum(results["restricted_costs"]), sum(results["company_overhead_allocation"]), sum(results["total_costs"])]
}

df = pd.DataFrame(data)
df.loc[len(df)] = ["Önköltség/db (eFt)", results["unit_costs"][0], results["unit_costs"][1], ""]
df.loc[len(df)] = ["Közvetlen önköltség (eFt/db)", results["direct_unit_costs"][0], results["direct_unit_costs"][1], ""]
df.loc[len(df)] = ["Szűkített önköltség (eFt/db)", results["restricted_unit_costs"][0], results["restricted_unit_costs"][1], ""]

# Eredmények kiírása a konzolba
print(df)
