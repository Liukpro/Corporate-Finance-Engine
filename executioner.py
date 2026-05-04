from yahoo_fetcher import fetch_financials
from resolver import resolve_inputs
from formulas import *

def main(ticker):

    raw = fetch_financials(ticker)

    data = resolve_inputs(raw)

    mol = calc_mol(data["ric_op_mon"], data["cost_op_mon"])
    rol = calc_rol_from_mol(mol, data["ammort"])

    print(f"MOL (Margine Operativo Lordo): {mol:,.0f}")
    print(f"ROL (Risultato Operativo Lordo): {rol:,.0f}")

if __name__ == "__main__":
    main("RACE")
