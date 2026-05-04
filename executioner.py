from yahoo_fetcher import fetch_financials
from dag_resolver import resolve_inputs
from dag_calculator import *

def main(ticker):

    raw = fetch_financials(ticker)

    data = resolve_inputs(raw)

    mol = calc_mol(data["ric_op_mon"], data["cost_op_mon"])
    rol = calc_rol_from_mol(mol, data["ammort"])

    print(mol, rol)

if __name__ == "__main__":
    main("RACE")
