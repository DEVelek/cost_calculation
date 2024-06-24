import pandas as pd

def calculate_costs(direct_material_cost, direct_labor_cost, other_direct_cost, production_units, operating_overhead, company_overhead, operating_base="material", company_base="restricted"):
    """
    Calculate various costs associated with production.

    Parameters:
    - direct_material_cost (list): Costs for materials.
    - direct_labor_cost (list): Costs for labor.
    - other_direct_cost (list): Other direct costs.
    - production_units (list): Number of units produced.
    - operating_overhead (float): Total operating overhead.
    - company_overhead (float): Total company overhead.
    - operating_base (str): Basis for operating overhead allocation.
    - company_base (str): Basis for company overhead allocation.

    Returns:
    - dict: Calculated costs and allocations.
    """
    # Summing up direct costs
    total_direct_cost = [a + b + c for a, b, c in zip(direct_material_cost, direct_labor_cost, other_direct_cost)]

    # Allocating operating overhead
    base_operating = select_base(operating_base, direct_material_cost, direct_labor_cost, other_direct_cost, total_direct_cost)
    total_base_operating = sum(base_operating)
    operating_overhead_allocation = [bo / total_base_operating * operating_overhead for bo in base_operating]

    # Summing up restricted costs
    restricted_costs = [tdc + oha for tdc, oha in zip(total_direct_cost, operating_overhead_allocation)]

    # Allocating company overhead
    base_company = select_base(company_base, direct_material_cost, direct_labor_cost, other_direct_cost, restricted_costs, total_direct_cost)
    total_base_company = sum(base_company)
    company_overhead_allocation = [bc / total_base_company * company_overhead for bc in base_company]

    # Summing up total costs
    total_costs = [rc + coa for rc, coa in zip(restricted_costs, company_overhead_allocation)]

    # Calculating unit costs
    unit_costs = [tc / pu for tc, pu in zip(total_costs, production_units)]
    direct_unit_costs = [tdc / pu for tdc, pu in zip(total_direct_cost, production_units)]
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

def select_base(base_type, direct_material_cost, direct_labor_cost, other_direct_cost, restricted_costs, total_direct_cost=None):
    """
    Select the base for overhead allocation.

    Parameters:
    - base_type (str): The type of base for allocation.
    - direct_material_cost (list): Costs for materials.
    - direct_labor_cost (list): Costs for labor.
    - other_direct_cost (list): Other direct costs.
    - restricted_costs (list): Restricted costs.
    - total_direct_cost (list): Total direct costs.

    Returns:
    - list: Selected base costs.
    """
    if base_type == "material":
        return direct_material_cost
    elif base_type == "labor":
        return direct_labor_cost
    elif base_type == "other":
        return other_direct_cost
    elif base_type == "direct":
        return total_direct_cost
    elif base_type == "restricted":
        return restricted_costs
    else:
        raise ValueError("Invalid base type. Please choose 'material', 'labor', 'other', 'direct', or 'restricted'.")

def parse_input(prompt, language, is_float=True):
    """
    Parse input values from the user.

    Parameters:
    - prompt (str): The prompt message.
    - language (str): The language of the prompt.
    - is_float (bool): Whether to parse as float or not.

    Returns:
    - list: Parsed input values.
    """
    while True:
        try:
            print(prompt)
            values = input().strip().split(',')
            return [float(value) if is_float else value for value in values]
        except ValueError:
            print("Invalid input. Please try again.")

def get_user_inputs(language):
    """
    Get user inputs based on the selected language.

    Returns:
    - list: Parsed input values.
    """
    prompts = [
        ("Adja meg a közvetlen anyagköltséget a termékekhez (pl. 600,400,300):", "Enter Direct material cost for products (e.g., 600,400,300):"),
        ("Adja meg a közvetlen bérköltséget a termékekhez (pl. 300,200,100):", "Enter Direct labor cost for products (e.g., 300,200,100):"),
        ("Adja meg az egyéb közvetlen költséget a termékekhez (pl. 420,320,220):", "Enter Other direct cost for products (e.g., 420,320,220):"),
        ("Adja meg az előállított termékek számát (pl. 10,20,30):", "Enter Production units for products (e.g., 10,20,30):"),
        ("Adja meg az üzemi általános költséget (pl. 500):", "Enter Operating overhead (e.g., 500):"),
        ("Adja meg a vállalati általános költséget (pl. 810):", "Enter Company overhead (e.g., 810):")
    ]

    direct_material_cost = parse_input(prompts[0][0] if language == "hungarian" else prompts[0][1], language)
    direct_labor_cost = parse_input(prompts[1][0] if language == "hungarian" else prompts[1][1], language)
    other_direct_cost = parse_input(prompts[2][0] if language == "hungarian" else prompts[2][1], language)
    production_units = parse_input(prompts[3][0] if language == "hungarian" else prompts[3][1], language)
    operating_overhead = float(parse_input(prompts[4][0] if language == "hungarian" else prompts[4][1], language)[0])
    company_overhead = float(parse_input(prompts[5][0] if language == "hungarian" else prompts[5][1], language)[0])
    
    return direct_material_cost, direct_labor_cost, other_direct_cost, production_units, operating_overhead, company_overhead

def validate_inputs(operating_base, company_base):
    """
    Validate the input bases for overhead allocation.

     Parameters:
    - operating_base (str): The operating overhead base.
    - company_base (str): The company overhead base.
    
    Raises:
    - ValueError: If an invalid base is provided.
    """
    valid_operating_bases = ["material", "labor", "other", "direct"]
    valid_company_bases = ["restricted", "direct"]
    
    if operating_base not in valid_operating_bases:
        raise ValueError("Invalid operating base. Please choose 'material', 'labor', 'other', or 'direct'.")
    if company_base not in valid_company_bases:
        raise ValueError("Invalid company base. Please choose 'restricted' or 'direct'.")

def main():
    try:
        # Choose language
        print("Choose the output language ('english' or 'hungarian'):")
        language = input().strip().lower()

        # Number of products
        print("Enter the number of products (minimum 2):" if language == "english" else "Adja meg a termékek számát (minimum 2):")
        num_products = int(input().strip())
        if num_products < 2:
            num_products = 2

        # Get user inputs
        direct_material_cost, direct_labor_cost, other_direct_cost, production_units, operating_overhead, company_overhead = get_user_inputs(language)

        # Input allocation bases
        operating_base_prompt = "Enter the allocation base for operating overhead ('material', 'labor', 'other' or 'direct'):" if language == "english" else "Adja meg az üzemi általános költségek vetítési alapját ('material' - anyag, 'labor' - bér, 'other' - egyéb, 'direct' - közvetlen) (kérem angolul adja meg):"
        company_base_prompt = "Enter the allocation base for company overhead ('restricted' or 'direct'):" if language == "english" else "Adja meg a vállalati általános költségek vetítési alapját ('restricted' - szűkített, 'direct' - közvetlen) (kérem angolul adja meg):"

        operating_base = parse_input(operating_base_prompt, language, is_float=False)[0].strip().lower()
        company_base = parse_input(company_base_prompt, language, is_float=False)[0].strip().lower()

        # Validate inputs
        validate_inputs(operating_base, company_base)

        # Calculate costs
        results = calculate_costs(direct_material_cost, direct_labor_cost, other_direct_cost, production_units, operating_overhead, company_overhead, operating_base, company_base)

        # Prepare data for display
        if language == "hungarian":
            data = {
                "Megnevezés": ["Közvetlen anyagköltség", "Közvetlen bérköltség", "Egyéb közvetlen költség", "Összes közvetlen költség", "Üzemi általános költség", "Szűkített költség", "Vállalati általános költség", "ÖSSZES KÖLTSÉG"],
                **{f"A termék {chr(65+i)} (eFt)": [direct_material_cost[i], direct_labor_cost[i], other_direct_cost[i], results["total_direct_cost"][i], results["operating_overhead_allocation"][i], results["restricted_costs"][i], results["company_overhead_allocation"][i], results["total_costs"][i]] for i in range(num_products)},
                "Vállalati összesen (eFt)": [sum(direct_material_cost), sum(direct_labor_cost), sum(other_direct_cost), sum(results["total_direct_cost"]), sum(results["operating_overhead_allocation"]), sum(results["restricted_costs"]), sum(results["company_overhead_allocation"]), sum(results["total_costs"])]
            }
            df = pd.DataFrame(data)

            unit_cost_data = {
                "": ["Közvetlen önköltség (eFt/db)", "Szűkített önköltség (eFt/db)", "Önköltség/db (eFt)"],
                **{f"A termék {chr(65+i)}": [results["direct_unit_costs"][i], results["restricted_unit_costs"][i], results["unit_costs"][i]] for i in range(num_products)}
            }
            unit_cost_df = pd.DataFrame(unit_cost_data)

        else:
            data = {
                "Description": ["Direct material cost", "Direct labor cost", "Other direct cost", "Total direct cost", "Operating overhead", "Restricted cost", "Company overhead", "TOTAL COST"],
                **{f"Product {chr(65+i)} (thousand HUF)": [direct_material_cost[i], direct_labor_cost[i], other_direct_cost[i], results["total_direct_cost"][i], results["operating_overhead_allocation"][i], results["restricted_costs"][i], results["company_overhead_allocation"][i], results["total_costs"][i]] for i in range(num_products)},
                "Company total (thousand HUF)": [sum(direct_material_cost), sum(direct_labor_cost), sum(other_direct_cost), sum(results["total_direct_cost"]), sum(results["operating_overhead_allocation"]), sum(results["restricted_costs"]), sum(results["company_overhead_allocation"]), sum(results["total_costs"])]
            }
            df = pd.DataFrame(data)

            unit_cost_data = {
                "": ["Direct unit cost (thousand HUF/unit)", "Restricted unit cost (thousand HUF/unit)", "Total unit cost (thousand HUF/unit)"],
                **{f"Product {chr(65+i)}": [results["direct_unit_costs"][i], results["restricted_unit_costs"][i], results["unit_costs"][i]] for i in range(num_products)}
            }
            unit_cost_df = pd.DataFrame(unit_cost_data)

        # Display results
        print(df)
        print(unit_cost_df)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
