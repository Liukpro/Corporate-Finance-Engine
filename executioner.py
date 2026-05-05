from yahoo_fetcher import fetch_financials
from resolver import resolve_inputs
from formulas import *

def main(ticker, year=None):

    raw = fetch_financials(ticker, year=year)

    print("_missing:", raw.get("_missing"))
    print("ric_op_mon:", raw.get("ric_op_mon"))
    print("cost_op_mon:", raw.get("cost_op_mon"))
    print("ammortamento:", raw.get("ammort"))
    print("_year:", raw.get("_year"))
    print("imp:", raw.get("imp"))

    data = resolve_inputs(raw)

    mol_list = []
    rol_list = []

    mol = calc_mol(data["ric_op_mon"], data["cost_op_mon"])
    rol = calc_rol_from_mol(mol, data["ammort"])

    mol_list.append(mol)
    rol_list.append(rol)

    print(f"MOL: {mol_list[-1]:,.0f}")
    print(f"ROL: {rol_list[-1]:,.0f}")

    fccnogc = calc_fccnogc_from_mol(mol_list[-1], data["tax"])
    print(f"FCCNOGC: {fccnogc:,.0f}")




if __name__ == "__main__":
    main("RACE", year = 2025)

if __name__ == "__main__":
    main("RACE", year = 2025)
